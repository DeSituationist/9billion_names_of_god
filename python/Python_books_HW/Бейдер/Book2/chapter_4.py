# Равенство и тожденственность
a = [1, 2, 3]
b = a
print(a, b)
print(a == b)
print(a is b) 
c = list(a)  # Создаем копию
print(c)
print(c == a)
print(c is a)
# __repr__ и __str__
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self): return f'{self.color} auto'
my_car = Car('red', 387281)
print(my_car)
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self): return '__repr__ for car object'
    def __str__(self): return '__str__ for car object'
my_car = Car('Red', 37281)
print(my_car)
print('{}'.format(my_car))
print(f'{my_car}')
print(str([my_car]))  # В контейнерах repr
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    #def __repr__(self): return f'Car({self.color!r}, {self.mileage!r})'  # !r чтобы использовались repr(self.color), а не str(self.color)
    def __repr__(self): return (f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})')
my_car = Car('Red', 37281)
print(my_car)
# Собственные классы исключений
def validate(name):
    if len(name) < 10: raise ValueError
class NameTooShort(ValueError):
    pass
def validate(name):
    if len(name) < 10: raise NameTooShort  # Более понятное исключение
class BaseValidationError(ValueError):
    pass
class NameTooLongError(BaseValidationError):
    pass
class NameTooCuteError(BaseValidationError):
    pass
'''
try:
    validate(name)
except BaseValidationError as err:
    handle_validation_error(err)
'''
# Копирование объектов, чтобы не изменять оригинал по иному имени
'''
new_list = list(original_list)
new_dict = dict(oridinal_dict)
new_set = set(original_set)
'''
# Мелкое/поверхностное копирование
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
print(xs, ys)
xs.append(['New list'])
print(ys)
xs[1][0] = 'X'
print(xs, ys)
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
print(xs, zs)
xs[1][0] = 'X'
print(xs, zs)
# Копирование объектов собственных классов
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'
a = Point(23, 42)
b = copy.copy(a)
print(a, b)
print(a is b)
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
    def __repr__(self):
        return f'Rectangle({self.topleft!r}, {self.bottomright!r})'
rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
print(rect)
print(srect)
print(srect is rect)
rect.topleft.x = 999
print(rect, srect)
drect = copy.deepcopy(srect)
drect.topleft.x = 222
print(drect)
print(rect)
print(srect)  # __copy__ и __deepcopy__ можно переопределять в собственных классах для управления копированием
# Абстрактные класса
from abc import ABCMeta, abstractmethod
# Позволяет избежать создание экземпляров базового класса и проверяет переопредление метода в дочерних на ранних стадиях
class Base(metaclass = ABCMeta):
    @abstractmethod
    def foo(self) : pass
    @abstractmethod
    def bar(self) : pass
class Concrete(Base):
    def foo(self) : pass
    # bar забыли объявить
#c = Concrete()  #  TypeError: Can't instantiate abstract class Concrete without an implementation for abstract method 'bar'
# Именованые кортежи namedtuple
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car.mileage)
print(my_car[0])
print(tuple(my_car))
print(*my_car)
print(my_car)
class MyCarWithMethods(Car):  # Расширение класса namedtuple своим методом
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'
c = MyCarWithMethods('red', 3812.4)
print(c.hexcolor())
# Добавление новых полей
Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('power', ))
print(ElectricCar('red', 3812.4, 45.0))
# _asdict - возвращает значения в виде словаря
print(my_car._asdict()) 
# json.dumps(my_car._asdict()) - повзволяет избежать неправильных имен
# _replace - создает поверхностную копию и заменяет поля
print(my_car._replace(color='blue'))
# _make - создает новый namedtuple из итератора
print(Car._make(['red', 999]))
# Переменные класса и переменные экземпляра
class Dog:
    num_legs = 4  # Переменная класса
    def __init__(self, name):
        self.name = name  # Переменная экземпляра
jack = Dog('jack')
jill = Dog('jill')
print(jack.name, jill.name)
jack.num_legs = 6  # Создает локальную переменную с именем num_legs закрывая переменную класса
print(jack.num_legs, jack.__class__.num_legs)
class CountedObject:
    num_instances = 0  # Счетчик использований
    def __init__(self):
        self.__class__.num_instances += 1
# Методы класса, экземпляра и статические
class MyClass:
    def method(self): return 'Called object method', self
    @classmethod
    def classmethod(cls): return 'called class method', cls
    @staticmethod
    def staticmethod(): return 'called static method'
obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
# Вызов без экземпляра
print(MyClass.classmethod())
print(MyClass.staticmethod())
#print(MyClass.method())  # TypeError: MyClass.method() missing 1 required positional argument: 'self'
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
print(Pizza(['cheese', 'tomato']))
# Используем фабричные функции в классе для создания разных пицц
import math
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    @classmethod
    def margherita(cls):
        return cls(['mozzarela', 'tomato'])
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarela', 'tomato', 'ham'])
print(Pizza.margherita())
print(Pizza.prosciutto())
class Pizza:
    def __init__(self, radius,ingredients):
        self.ingredients = ingredients
        self.radius = radius
    def __repr__(self) : return f'Pizza {self.radius!r}, {self.ingredients!r}'
    def area(self) : return self.circle_area(self.radius)
    @staticmethod
    def circle_area(r):  # Удобен для тестирования
        return r ** 2 ** math.pi