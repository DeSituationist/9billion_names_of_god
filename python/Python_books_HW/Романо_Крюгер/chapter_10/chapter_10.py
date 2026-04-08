# api
from pathlib import Path
import csv
from copy import deepcopy

from marshmallow import Schema, fields, pre_load
from marshmallow.validate import Length, Range

class UserSchema(Schema):
    '''Представляет валидного пользователя'''
    email = fields.Email(required=True)
    name = fields.Str(required=True, validate=Length(min=1))
    age = fields.Int(required=True, validate=Range(min=18, max=65))
    role = fields.Str()

    @pre_load()
    def strip_name(self, data, **kwargs):
        data_copy = deepcopy(data)
        try:
            data_copy['name'] = data_copy['name'].strip()
        except (AttributeError, KeyError, TypeError): pass
        return data_copy
schema = UserSchema()

def is_valid(user):
    """Проверяет, является ли пользователь валидным."""
    return not schema.validate(user)

def get_valid_users(users):
    '''Возвращает по одному валидному пользователю из списка users.'''
    yield from filter(is_valid, users)

def export(filename, users, overwrite = True):
    '''Экспортировать CSV-файл. Создает CSV-файл и заполняет его валидными пользователями. 
    Если параметр overwrite равен False и файл уже существует, то вызывается ошибка IOError.'''
    if not overwrite and Path(filename).isfile():
        raise IOError(f'{filename} already exists.')
    valid_users = get_valid_users(users)
    write_csv(filename, valid_users)

def write_csv(filename, users):
    '''Записать CSV-файл с заданным именем и списком пользователей.
    Пользователи считаются валидными для структуры этого CSV.'''
    fieldnames = ['email', 'name', 'age', 'role']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)
from unittest.mock import patch, mock_open, call
import pytest
# tests
@pytest.fixture
def min_user():
    """Представляет валидного пользователя с минимальным набором данных."""
    return {
        'email': 'minimal@example.com',
        'name': 'Primus Minimus',
        'age': 18,
    }
@pytest.fixture
def full_user():
    """Представляет валидного пользователя с полным набором данных."""
    return {
        'email': 'full@example.com',
        'name': 'Maximus Plenis',
        'age': 65,
        'role': 'emperor',
    }
@pytest.fixture
def users(min_user, full_user):
    """Список пользователей: два валидных и один невалидный."""
    bad_user = {
        'email': 'invalid@example.com',
        'name': 'Horribilis',
    }
    return [min_user, bad_user, full_user]
class TestIsValid:
    """Проверка, как код определяет валидность пользователя."""
    def test_minimal(self, min_user):
        assert is_valid(min_user)
    def test_full(self, full_user):
        assert is_valid(full_user)
    @pytest.mark.parametrize('age', range(18))
    def test_invalid_age_too_young(self, age, min_user):
        min_user['age'] = age
        assert not is_valid(min_user)
    @pytest.mark.parametrize('age', range(18, 66))
    def test_valid_age(self, age, min_user):
        min_user['age'] = age
        assert is_valid(min_user)
    @pytest.mark.parametrize('field', ['email', 'name', 'age'])
    def test_mandatory_fields_empty(self, field, min_user):
        min_user['field'] = ''
        assert not is_valid(min_user)
    @pytest.mark.parametrize(
    ('email', 'outcome'), 
    [
    ("missing_at.com", False),
    ("@missing_start.com", False),
    ("missing_end@", False),
    ("missing_dot@example", False),
    ("good.one@example.com", True),
    ("δοκιμή@παράδειγμα.δοκιμή", True),
    ("аджай@экзампл.рус", True),
    ])
    def test_email(self, email, outcome, min_user):
        """Проверка различных форматов адресов электронной почты."""
        min_user['email'] = email
        assert is_valid(min_user) == outcome
# tests for export
class TestExport:
    """Проверка поведения функции export."""
    @pytest.fixture
    def csv_file(self, tmp_path):
        """Подготовить имя файла во временной папке.
        Благодаря механизму фикстуры tmp_path в pytest
        сам файл еще не существует.
        """
        csv_path = tmp_path / 'out.csv'
        yield csv_path
        csv_path.unlink(missing_ok=True)
    @pytest.fixture
    def exsisting_file(self, tmp_path):
        """Создать временный файл и записать в него содержимое."""
        existing = tmp_path / 'exsisting.csv'
        existing.write_text('Please leave me alone')
        return existing
    def test_export(self, users, csv_file):
        export(csv_file, users)
        text = csv_file.read_text()
        assert (
            'email,name,age,role\n'
            'minimal@example.com,Primus Minimus,18,\n'
            'full@example.com,Maximus Plenis,65,emperor\n'
        ) == text