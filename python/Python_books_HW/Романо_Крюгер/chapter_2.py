# mutable и immutable
age = 42
print(id(age))
age = 43
print(id(age))
numbers = set()
print(id(numbers))
numbers.add(3)
numbers.add(7)
print(id(numbers))
print(numbers)
# int
a = 14
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(7 / 4)
print(7 // 4)
print(- 7 / 4)
print(-7 // 4)  # python всегда округляет в меньшую сторону, то есть к -inf
print(int(7 / 4)) 
print(int(-7 / 4))  # отбрасывает дробную часть
print(pow(123, 4))
print(pow(123, 4, 100))  # возведение в степень по модулю
print(pow(37, -1, 43))  # возведение в -1 степень дает обратное число
# bool
# Является подклассом int
print(int(True))
print(int(False))
print(bool(1))
print(bool(-42))
print(0)
print(not True)
print(not False)
print(True and True)
print(False and True)
# float
pi = 3.1415926536
radius = 4.5
area = pi * (radius ** 2)
print(area)
import sys
print(sys.float_info)
# complex
c = 3.14 + 2.73j
c = complex(3.14, 2.73)
print(c.real)
print(c.imag)
print(c.conjugate)  # сопряженное
print(c * 2)
print(c ** 2)
d = 1 + 1j
print(c - d)
# fraction и decimal
from fractions import Fraction
print(Fraction(10, 6))
print(Fraction(1, 3) + Fraction(2, 3))
f = Fraction(10, 6)
print(f.numerator)  # числитель
print(f.denominator)  # знаминатель
print(f.as_integer_ratio())
from decimal import Decimal as D
print(D(3.14))
print(D('3.14'))
print(D(0.1) * D(3) - D(0.3))
print(D('0.1') * D(3) - D('0.3'))
# str и byte
str1 = 'This is a string. We built it with single quotes.'
str2 = "This is also a string, but built with double quotes."
str3 = '''This is built sing triple quptes,
so it can span multiple lines.'''
str4 = """This too
is a multiline one
built with triple double-quotes."""
print(repr(str4))
print(str4)
s = 'Hello there'
print(s.removeprefix('Hell'))
print(s.removesuffix('here'))
print(s.removeprefix('Prefix'))
s = 'This is üŋíc0de'
print(type(s))
encoded_s = s.encode('utf-8')
print(encoded_s)
print(type(encoded_s))
print(encoded_s.decode('utf-8'))
s = 'The trouble is you think you have time'
print(s[0], s[5])
print(s[:4], s[4:])
print(s[2:14], s[2:14:3])
print(s[:])
greet_old = 'Hello %s!'
print(greet_old%'Fabrizio')
greet_positional = 'Hello {}'
print(greet_positional.format('Fabrizio'))
greet_positional = 'Hello {} {}'
print(greet_positional.format('Fabrizio', 'Romano'))
greet_positional_idx = 'This is {0}! {1} loves {0}'
print(greet_positional_idx.format('Python', 'Heinrich'))
print(greet_positional_idx.format('Coffee', 'Fab'))
keyword = 'Hello, my name is {name} {last_name}'
print(keyword.format(name='Fabrizio', last_name='Romano'))
name = 'Fab'
age = 48
print(f'Hello! My name is {name} and i\'m {age}')
user = 'heinrich'
password = 'super-secret'
print(f'Log in with: {user} and {password}')
print(f'Log in with {user=} and {password=}')
languages = ['Python', 'Javascript']
print(f'Two very popular languages: {', '.join(languages)}')
print(f'Who knew f-strings could be so powerful? {'\N{shrug}'}')
# tuple
t = ()
print(type(t))
one_element_tuple = (42, )
three_elements_tuple = (1, 3, 5)
a, b, c = 1, 2, 3
print(a, b, c)
print(3 in three_elements_tuple)
a, b = 1, 2
c = a
a = b
b = c
print(a, b)
a, b = 0, 1
a, b = b, a  # обмен значениями через кортеж
print(a, b)
# list
print([], list(), [1, 2, 3])
print([x + 5 for x in [2, 3, 4]])
print(list((1, 3, 5, 7, 9)))
print(list('hello'))
a = [1, 2, 1, 3]
a.append(13)
print(a)
print(a.count(1))
a.extend([5, 7])
print(a)
print(a.index(13))
a.insert(0, 17)
print(a)
a.pop()
a.pop(3)
print(a)
a.remove(17)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.clear()
print(a)
a = list('Hello')
print(a)
a.append(100)
print(a)
a.extend((1, 2, 3))
print(a)
a.extend('...')
print(a)
a = [1, 3, 5, 7]
print(min(a))
print(max(a))
print(sum(a))
from math import prod
print(prod(a))  # Произведение всех значений в списке
print(len(a))
b = [6, 7, 8]
print(a + b)
print(a * 2)
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
print(sorted(a))
print(sorted(a, key=itemgetter(0)))
print(sorted(a, key=itemgetter(0, 1)))
print(sorted(a, key=itemgetter(1)))
print(sorted(a, key=itemgetter(0), reverse=True))
# bytearray
print(bytearray())
print(bytearray(10))
print(bytearray(range(5)))
name = bytearray(b'Lina')
print(name.replace(b'L', b'1'))
print(name.endswith(b'na'))
print(name.upper())
print(name.count(b'L'))
# set/frozenset
small_primes = set()
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes)
small_primes.add(1)
print(small_primes)
small_primes.remove(1)
print(3 in small_primes)
print(4 in small_primes)
small_primes.add(3)
print(small_primes)
biggger_primes = set([5, 7, 11, 13])
print(small_primes | biggger_primes)
print(small_primes & biggger_primes)
print(small_primes - biggger_primes)
small_primes = {2, 3, 5, 5}
print(small_primes)
small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])
#small_primes.add(11)  # AttributeError: 'frozenset' object has no attribute 'add'
#small_primes.remove(2)  # AttributeError: 'frozenset' object has no attribute 'remove'
print(small_primes & bigger_primes)
# dict
a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})
print(a == b == c == d == e)
print(list(zip(list('Hello'), list(range(1, 6)))))
d = {}
d['a'] = 1
d['b'] = 2
print(len(d))
print(d['a'])
print(d)
del d['a']
print(d)
d['c'] = 3
print('c' in d)
print(3 in d)
print('e' in d)
d.clear()
print(d)
d = dict(zip('hello', range(5)))
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(3 in d.values())
print(('o', 4) in d.items())
print(d)
d.popitem()
print(d)
print(d.pop('l'))
#d.pop('not-a-key')  # KeyError: 'not-a-key'
print(d.pop('not-a-key', 'default-val'))
d.update({'another': 'value'})
d.update(a=13)
print(d)
print(d.get('a'))
print(d.get('a', 177))
print(d.get('b', 177))
print(d.get('b'))
d = {}
d.setdefault('a', 1)
print(d)
d.setdefault('a', 5)  # Возвращает значение
print(d)
d = {}
d.setdefault('a', {}).setdefault('b', []).append(1)
print(d)
d = {'a': 'A', 'b': 'B'}
e = {'b': 8, 'c': 'C'}
print(d | e)
print(e | d)
print({**d, **e})
print({**e, **d})
d |= e
print(d)
# date и time
from datetime import date, datetime, timedelta, timezone, UTC
import time
import calendar as cal
today = date.today()
print(today)
print(today.ctime())
print(today.isoformat())
print(today.weekday())
print(cal.day_name[today.weekday()])
print(today.day, today.month, today.year)
print(today.timetuple())
print(time.ctime())
print(time.daylight)
print(time.gmtime())
print(time.gmtime(0))  # 1 января 1970 - Эпоха, операцинная система ведет отсчет с этого момента
print(time.localtime())
print(time.time())
now = datetime.now()
utcnow = datetime.now(UTC)
print(now)
print(utcnow)
print(now.date())
print(now.day, now.month, now.year)
print(now.date() == date.today())
print(now.time())
print(now.hour, now.minute, now.second, now.microsecond)
print(now.ctime())
print(now.isoformat())
print(now.timetuple())
print(now.tzinfo)  # Информация о временной зоне
print(utcnow.tzinfo)
print(now.weekday())
f_bday = datetime(1975, 12, 29, 12, 50, tzinfo=timezone(timedelta(hours=2)))
h_bday = datetime(1981, 10, 7, 15, 30, 50, tzinfo=timezone(timedelta(hours=2)))
diff = h_bday - f_bday
print(type(diff))
print(diff.days)
print(diff.total_seconds())
print(today + timedelta(days=49))
print(now + timedelta(weeks=7))
print(datetime.fromisoformat('1977-11-24T19:30:13+01:00'))  # Берем время из ISO строки
# namedtuple
from collections import namedtuple
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
print(vision[0])
print(vision.left)
print(vision.right)
Vision = namedtuple('Vision', ['left', 'combined','right'])
vision = Vision(9.5, 9.2,8.8)
print(vision.left)
print(vision.combined)
print(vision.right)
# defaultdict
d = {}
d['age'] = d.get('age', 0) + 1
print(d)
d = {'age': 39}
d['age'] = d.get('age', 0) + 1
print(d)
from collections import defaultdict
dd = defaultdict(int)
dd['age'] += 1
print(dd)
# Chainmap
from collections import ChainMap
default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port': 5678}
conn = ChainMap(connection, default_connection)
print(conn['port'])
print(conn['host'])
print(conn.maps)
del conn['port']
print(conn.maps)
print(conn['port'])
print(dict(conn))
# enum
GREEN = 1
YELLOW = 2
RED = 4
TRAFFIC_LIGHTS = (GREEN, YELLOW, RED)
print(type(TRAFFIC_LIGHTS), type(GREEN))
from enum import Enum
class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 3
print(repr(TrafficLight.GREEN))
print(TrafficLight.GREEN.value)
# Кеширования малых значений в python
a = 100_000_000 ** 20
b = 100_000_000 ** 20
print(id(a) == id(b))
a = 5
b = 5
print(id(a) == id(b))  # Интернирование объектов ( неизменяемых типов данных )
'''
Какой доступ нам нужен?
Какие операции придется выполнять над элементами? Как часто?
Будет ли коллекция изменяться co временем?
Нужно ли будет модифицировать словари клиентов?
Какая операция c коллекцией будет выполняться чаще всего?
'''