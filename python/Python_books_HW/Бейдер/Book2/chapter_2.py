# Assert
def apply_discount(product, discount):
    price = int(product['цена'] * (1.0 - discount))
    assert 0 <= price <= product['цена']
    return price
shoes = {'имя': 'Модные туфли', 'цена': 14900}
print(apply_discount(shoes, 0.25))
'''
print(apply_discount(shoes, 2.0))
#Так как assert может быть отключен и превращаться в нулевую операцию
#его нельзя использовать для проверки входных данных
def delete_product(prod_id, user):
    assert user.is_admin()
    assert store.has_product(prod_id)
    store.get_product(prod_id).delete()
#Правильная проверка
def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('Для удаления необходимы права администратора')
    if not store.has_product(product_id):
        raise ValueError('Идентификатор неизвестного товара')
    store.get_product(product_id).delete()
'''
assert(1 == 2, 'Это утверждение должно вызвать сбой')  # Кортежное выражение, так как не пустой кортеж всегда дает True
# Запятые
names = ['Элис', 'Боб', 'Дилберт']  # При изменении человек использовавший git diff может не заметить разницу
names = [
    'Элис',
    'Боб',
    'Дилберт',
]  # Удобнее видеть изменения по строкам
# менеджер контекста with
with open('hello.txt', 'w') as f:
    ...
# Вместо 
f = open('hello.txt', 'w')
try:
    f.write('привет, мир')
finally:
    f.close()
some_lock = threading.Lock()
with some_lock:
    ...
# Вместо
some_lock.acquire()
try:
    ...
finally:
    some_lock.realease()
# Собственный менеджер контекста (интерфейс)
# Нужно добавить в класс методы __enter__ и __exit__
class ManagedFile:  # Поддерживает конструкцию with
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file: self.file.close()
with ManagedFile('hello.txt') as f:
    f.write('hello world')
    f.write('And now bye world')
# Используя декоратор
from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()
with managed_file('hello.txt') as f:
    f.write('hello world')
    f.write('And now bye world')
# API с помощью менеджера контекстов
class Indenter:
    def __init__(self):
        self.level = 0
    def __enter__(self):
        self.level += 1
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
    def print(self, text):
        print(' ' * self.level + text)
with Indenter() as indent:
    indent.print('Hello')
    with indent:
        indent.print('great')
        with indent:
            indent.print('bounjur')
        indent.print('hey')
_var = 1  # Предназначено для внутреннего пользования
# При импортированни модуля через * данные имена не будет импортироваться без __all__
class_ = 'Class'  # Используется чтобы избежать совпадения с зарезервированными именами Python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23  # Преобразуется в _Test__baz искажение имени
#                        # Используется для избежания переопределения в подклассах
class ExtendedTest(Test):
    def __init__(self):
        self.foo = 'changed'
        self._bar = 'changed'
        self.__baz = 'changed'  # Превратиться в _ExtendedTest__baz искажение имени 
#                               # При этом можно обратиться и к _Test__baz экземпляра подкласса
class ManglingTest:
    def __init__(self):
        self.__mangled = 'Hello'
    def get_mangled(self):
        return self.__mangled
ManglingTest().get_mangled()  # Обращение через метод
ManglingTest().__mangled  # Обращение к атрибуту выдаст ошибку
class MangledMethod:
    def __method(self):  
        return 42
    def call_it(self):
        return self.__method()
MangledMethod().__method()  # Обращение к напрямую методу даст ошибку
MangledMethod().call_it()  # Обращение через дополнительный метод работает
# double underscores - dunders
for _ in range(43): print('Yo')  # Исплользуется _ чтобы показать временность переменной
car = ('красный', 'легковой автомобиль', 12, 3812.4)
color, _, _, mileage = car  # Используется чтобы получить только нужные имена, а _ как заполнитель
# Форматирование строк
errno = 50159747054
name = 'Bob'
# Хотим получить 'Hey, Bob! Here is mistake 0xbadc0ffee!'
# Первый способ
print('Hey, %(name)s! Here is mistake 0x%(errno)x!'%{'name': name, 'errno': errno})
# Второй способ
print('Hey, {name}! Here is mistake 0x{errno:x}!'.format(name=name, errno=errno))
# Третий способ
print(f'Hey, {name}! Here is mistake {errno:#x}!')
# При обработке ввода пользователя использовать from string import Template