# open()
fh = open('fear.txt')
try:
    for line in fh:
        print(line.strip())
finally: fh.close()
# open with
with open('fear.txt') as fh:
    for line in fh:
        print(line.strip())
# print in file
with open('print_example.txt', 'w') as fw:
    print('Hey i am printing into a file!!!', file=fw)
with open('fear.txt') as f:
    lines = [line.strip() for line in f]
with open('fear_copy.txt', 'w') as fw:
    fw.write('\n'.join(lines))
'''
'x' - защита от презаписи
with open("write_x.txt", "x") as fw: # сработает
    fw.write("Writing line 1")
with open("write_x.txt", "x") as fw: # вызовет ошибку
    fw.write("Writing line 2")
'''
from collections import Counter
from string import ascii_letters
chars = ascii_letters + ' '
def sanitize(s, chars): return ''.join(c for c in s if c in chars)
def reverse(s): return s[::-1]
with open('fear.txt') as stream:
    lines = [line.rstrip() for line in stream]
with open('raef.txt', 'w') as stream:
    stream.write('\n'.join(reverse(line) for line in lines))
lines = [sanitize(line, chars) for line in lines]
whole = ' '.join(lines)
cnt = Counter(whole.lower().split())
print(cnt.most_common(3))
# Создание времменных каталогов и файлов на время теста
from tempfile import NamedTemporaryFile, TemporaryDirectory
with TemporaryDirectory(dir='.') as td:
    print('Temp directory:', td)
    with NamedTemporaryFile(dir=td) as t:
        name = t.name
        print(name)
# zip files
from zipfile import ZipFile
with ZipFile('example.zip', 'w') as zp:
    #zp.write('content1.txt')
    #zp.write('content2.txt')
    #zp.write('subfolder/content3.txt')
    #zp.write('subfolder/content4.txt')
    pass
# JSON
import sys
import json
data = {
    'big_number': 2 ** 3141,
    'max_float': sys.float_info.max,
    'a_list': [2, 3, 5, 7],
}
json_data = json.dumps(data)
data_out = json.loads(json_data)
assert data == data_out
info = {
    'Full_name': 'Sherlock Holmes',
    'address': {
        'street': '221b Baker st',
        'zip': 'NW1 6XE',
        'city': 'London',
        'country': 'UK',
    },
}
print(json.dumps(info, indent=2, sort_keys=True))
# Проблема сериализации типов, которых нет в json
data_in = {
    'a_tuple': (1, 2, 3, 4, 5),
}
json_data = json.dumps(data_in)
print(json_data)
data_out = json.loads(json_data)
print(data_out)

class ComplexEndcoder(json.JSONEncoder):
    def default(self, obj):
        print(f'ComplexEncoder.default: {obj=}')
        if isinstance(obj, complex):
            return {
                '_meta': 'complex',
                'num': [obj.real, obj.imag],
            }
        return super().default() # для не комплексных чисел
data = {
    'an_int': 42,
    'a_float': 3.14159265,
    'a_complex': 3 + 4j,
}
json_data = json.dumps(data, cls=ComplexEndcoder)
print(json_data)
def object_hook(obj): # Десериализация из JSON
    print(f'obj_hook: {obj=}')
    try:
        if obj['_meta'] == 'complex':
            return complex(*obj['num'])
    except KeyError:
        return obj
data_out = json.loads(json_data, object_hook=object_hook)
print(data_out)
# String IO
# тестировать код, работающий с файловыми объектами, не создавая реальные файлы
import io
stream = io.StringIO()
stream.write('Learning Python Programming\n')
print('Become a Python ninja.', file=stream)
contents = stream.getvalue()
print(contents)
stream.close()
with io.StringIO() as stream:
    stream.write('Learning Python Programming\n')
    print('Become a Python ninja.', file=stream)
    contents = stream.getvalue()
    print(contents)
# HTTP-запрос
import requests
urls = {
    'get': "https://httpbin.org/get?t=learn+python+programming",
    "headers": "https://httpbin.org/headers",
    "ip": "https://httpbin.org/ip",
    "user-agent": "https://httpbin.org/user-agent",
    "UUID": "https://httpbin.org/uuid",
    "JSON": "https://httpbin.org/json",
}
def get_content(title, url):
    resp = requests.get(url)
    print(f'Response for {title}')
    print(resp.json())
for title, url in urls.items():
    get_content(title, url)
    print('-' * 20)
# POST - запрос
import requests
url = "https://httpbin.org/post"
data = dict(title="Learn Python Programming")
resp = requests.post(url, data=data)
print('Response for POST')
print(resp.json())
# SQLAlchemy
from sqlalchemy import ForeignKey, String, Integer, create_engine, select, func
from sqlalchemy.orm import (DeclarativeBase, Session, mapped_column, relationship)
class Base(DeclarativeBase):
    pass
class Person(Base): # Таблица 'person'
    __tablename__ = 'person'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    age = mapped_column(Integer)
    emails = relationship(
        'Email',
        back_populates='person',
        order_by='Email.email',
        cascade='all, delete-orphan'
    )
    def __repr__(self): return f'{self.name}(id={self.id})'
class Email(Base): # 'email'
    __tablename__ = 'email'
    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String)
    person_id = mapped_column(ForeignKey('person.id'))
    person = relationship('Person', back_populates='emails')
    def __str__(self): return self.email
    __repr__ = __str__
def display_info(session):
    emails = select(Email)
    print('All emails:')
    for email in session.scalars(emails):
        print(f'- {email.person.name} <{email.email}>')
    people = session.scalar(
        select(func.count()).select_from(Person)
    )
    emails = session.scalar(
        select(func.count()).select_from(Email)
    )
    print('Summary:')
    print(f' {people=}, {emails=}')
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
with Session(engine) as session:
    anakin = Person(name="Anakin Skywalker", age=32)
    obione = Person(name="Obi-Wan Kenobi", age=40)
    obione.emails = [
        Email(email="obi1@example.com"),
        Email(email="wanwan@example.com"),
    ]
    anakin.emails.append(Email(email="ani@example.com"))
    anakin.emails.append(Email(email="evil.dart@example.com"))
    anakin.emails.append(Email(email="vader@example.com"))
    session.add(anakin)
    session.add(obione)
    session.commit()
    obione = session.scalar(
        select(Person).where(Person.name.like("Obi%"))
    )
    print(obione, obione.emails)
    anakin = session.scalar(
        select(Person).where(Person.name == "Anakin Skywalker")
    )
    print(anakin, anakin.emails)
    display_info(session)