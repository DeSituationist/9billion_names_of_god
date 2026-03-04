# Функции
def yell(text): return text.upper() + '!'
bark = yell
print(bark('woof'))
del yell
try:
    print(yell('woof'))
except:
    print('called bark')
    print(bark('woof'))
funcs = [bark, str.lower, str.capitalize]
for f in funcs: print(f, f('hello'))
def greet(func):  # Функция более высокого порядка - принимает другие функции
    greeting = func('Hey, i am python programm')
    print(greeting)
greet(bark)
# Вложенные функции
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)
print(speak('Hello, World'))
def get_speak_func(volume):
    def whisper(text): return text.lower() + '...'
    def yell(text): return text.upper() + '!'
    if volume > 0.5: return yell
    else: return whisper
print(get_speak_func(0.3))
print(get_speak_func(0.7))
speak_func = get_speak_func(0.7)
print(speak_func('Hello'))
# Сохранения состояния/замыкание
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5: return yell
    else: return whisper
print(get_speak_func('Hello, world', 0.7)())
def make_adder(n):
    def add(x):
        return x + n
    return add
plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4))
print(plus_5(4))
# Создание объектов-функций с сохранением состояния
class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x
plus_3 = Adder(3)
print(plus_3(4))
print(callable(plus_3))
print(callable('Ello'))
# lambda функции
add = lambda x, y: x + y
print(add(5, 3))
print((lambda x, y: x + y)(5, 3))  # функция одного выражения
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x : x[1]))
def make_adder(n):
    return lambda x: x + n
plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4))
print(plus_5(4))
# Не использовать lambda
class Car:
    rev = lambda self: print('Boom')
    crash = lambda self: print('Bam')
my_car = Car()
my_car.crash()
print(list(filter(lambda x: x % 2 == 0, range(16))))
# Лучше использовать списковое включение
print([x for x in range(16) if x % 2 == 0])
# Декораторы в Python
def null_decorator(func): return func  # Простой декоратор
@null_decorator
def greet(): return 'Hello'
print(greet())
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
@uppercase
def greet(): return 'Hello!'  
print(greet())  # при вызове greet происходит присваивание имени greet = uppercase(greet), то есть greet = wrapper и затем вызов нового greet 
# Многочисленное декорирование
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper
def emphasis(func):
    def wrapper():
        return '<em>' + func() + '<em>'
    return wrapper
@strong
@emphasis
def greet(): return 'Hello!'
print(greet())  # Декораторы выполняются снизу вверх
# Декорирование функции с аргументами
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Traceback: called {func.__name__}() c {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'Traceback: function {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper
@trace
def say(name, line):
    return f'{name}: {line}'
print(say('Jane', 'Hello, world'))
import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper
@uppercase
def greet():
    '''Return greeting'''
    return 'Hello'
print(greet.__name__)
print(greet.__doc__)  #Метаданные функции сохранены благодаря functools.wraps
# *args **kwargs
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'
print(AlwaysBlueCar('Green', 48932).color)
def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function
@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)
greet('Hello', 'Bob')
# Распоковка аргументов
def print_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')
print_vector(0, 1, 0)
tuple_vec = (1, 0, 1)
listt_vec = [1, 0, 1]
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])
print_vector(*tuple_vec)
print_vector(*listt_vec)
genexpr = (x * x for x in range(3))
print_vector(*genexpr)
dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)