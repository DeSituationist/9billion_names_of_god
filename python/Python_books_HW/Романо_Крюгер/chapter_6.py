# decorators
from time import time
from functools import wraps
def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper
def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print(f'Result is too big {result}. Max allowed is 100')
        return result
    return wrapper
@measure
@max_result
def cube(n): return n ** 3
print(cube(2))
print(cube(5))
# decorators factory
print('-' * 15 + 'decorators factory' + '-' * 15)
def max_result(thresgold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > thresgold:
                print(f'Result is too big {result}. Max allowed is {thresgold}')
            return result
        return wrapper
    return decorator
@max_result(75)
def cube(n): return n ** 3
print(cube(5))
# OOP
class Person:
    species = 'Human'
print(Person.species)
Person.alive = True
print(Person.alive)
man = Person()
print(man.species)
print(man.alive)
Person.alive = False
print(man.alive)
man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)
class Square:
    side = 8
    def area(self): return self.side ** 2
sq = Square()
print(sq.area())
print(Square.area(sq))
sq.side = 10
print(sq.area())
class Price:
    def final_price(self, vat, discount = 0): return (self.net_price) * (100 + vat) / 100 - discount
p1 = Price()
p1.net_price = 100
print(p1.final_price(20, 10))
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    def area(self): return self.side_a * self.side_b
r1 = Rectangle(10, 4)
print(r1.side_a, r1.side_b)
print(r1.area())
r2 = Rectangle(7, 3)
print(r2.area())
# inheritance(is A) and composition(has A)
print('-' * 15 + 'inheritance' + '-' * 15)
class Engine:
    def start(self): pass
    def stop(self): pass
class ElectricEngine(Engine): pass
class V8Engine(Engine): pass
print('-' * 15 + 'composition' + '-' * 15)
class Car:
    engine_cls = Engine
    def __init__(self): self.engine = self.engine_cls()
    def start(self):
        print(
            f'Starting {self.engine.__class__.__name__} for '
            f'{self.__class__.__name__}... wroom wroom'
        )
        self.engine.start()
    def stop(self): self.engine.stop()
class RaceCar(Car): engine_cls = V8Engine
class CityCar(Car): engine_cls = ElectricEngine
class F1Car(RaceCar): pass
car = Car()
raceCar = RaceCar()
cityCar = CityCar()
f1car = F1Car()
cars = [car, cityCar, raceCar, f1car]
for car in cars: car.start()
# super
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages
class Ebook(Book):
    def __init__(self, title, publisher, pages, foramt_):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        self.format_ = foramt_
class Ebook(Book):
    def __init__(self, title, publisher, pages, foramt_):
        #Book.__init__(self, title, publisher, pages)
        super().__init__(title, publisher, pages)
        self.format_ = foramt_
ebook = Ebook("Learn Python Programming", "Packt Publishing", 500, "PDF")
print(ebook.title)
print(ebook.publisher) 
print(ebook.pages) 
print(ebook.format_)
# static methods
class StringUtil:
    @staticmethod
    def is_palindrome(s, case_intensitive=True):
        s = ''.join(c for c in s if c.isalnum())
        if case_intensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c-1]:
                return False
        return True
    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())
print(
    StringUtil.is_palindrome("Radar", case_intensitive=False)
)
print(StringUtil.is_palindrome("A nut for a jar of tuna"))
print(StringUtil.is_palindrome("Never Odd, Or Even!")) 
print(
    StringUtil.is_palindrome(
        "In Girum Imus Nocte Et Consumimur Igni"
    )
) 
print(
    StringUtil.get_unique_words(
        "I love palindromes. I really really love them!"
    )
)
# class methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)
    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)
p = Point.from_tuple((3, 7))
print(p.x, p.y)
q = Point.from_point(p)
print(q.x, q.y)
class StringUtil:
    @classmethod
    def is_palindrome(cls, s, case_insensitive=True): # Открытый метод, позволяет разделить логику
        # Работаем со строкой через скрытые статические методы
        s = cls._strip_string(s)
        if case_insensitive: s = s.lower()
        return cls._is_palindrome(s)
    @staticmethod
    def _strip_string(s): return ''.join(c for c in s if c.isalnum())
    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s) // 2):
            if s[c] != s[-c-1]:
                return False
            return True
    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())
print(StringUtil.is_palindrome("radar"))
print(StringUtil.is_palindrome("not a palindrome"))
# property decorator
# используется для проверки. Например, age в рамках от 18 до 99
class Person:
    def __init__(self, age): self.age = age
class PersonWithAccessors:
    def __init__(self, age):
        self._age = age
    def get_age(self):
        return self._age
    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')
class PersonPythonic:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')
person = PersonPythonic(39)
print(person.age)
person.age = 42 
print(person.age) 
# person.age = 100 ValueError: Age must be within [18, 99]
'''
Один из удобных вариантов применения свойства (property) — это случаи, когда
при обращении к атрибуту нужно выполнить некую инициализацию. Например,
когда необходимо подключиться к базе данных или выйти на внешний API.
'''
class Client:
    def __init__(self):
        print('Setting up the client')
    def query(self, **kwargs):
        print(f'Performing a query: {kwargs}')
class Manager: 
    @property
    def client(self): return Client() # Создание клиента при каждом запросе дорого
    def perform_query(self, **kwargs): return self.client.query(**kwargs)
class ManualCacheManager:
    @property
    def client(self):
        if not hasattr(self, '_client'): # Проверка наличия клиента у менеджера
            self._client = Client()
        return self._client
    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)
#cached property
from functools import cached_property
class CachedPropertyManager:
    @cached_property
    def client(self):
        return Client()
    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)
manager = CachedPropertyManager()
manager.perform_query(object_id=42)
manager.perform_query(name_ilike="%Python%")
del manager.client # Обновление клиента
manager.perform_query(age_gte=18)
# data class
from dataclasses import dataclass
@dataclass
class Body:
    '''Class that represents physical body'''
    name: str
    mass: float = 0.0
    speed: float = 1.0
    def kinetic_energy(self) -> float:
        return (self.mass * self.speed**2) / 2
body = Body("Ball", 19, 3.1415)
print(body.kinetic_energy()) 
print(body)
# iterators
class OddEven:
    def __init__(self, data):
        self._data = data
        self.indexes = list(range(0, len(data), 2)) + list(range(1, len(data), 2))
    def __iter__(self): return self
    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration
oddeven = OddEven('0123456789')
print("".join(c for c in oddeven))
oddeven = OddEven("ABCD")
it = iter(oddeven) 
print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it)) 