# Словари, ассоциативные массивы и хеш-таблицы
# dict
phonebook = {
    'Bob': 7187,
    'Ellis': 3719,
    'Jack': 7052,
}
squares = {x: x * x for x in range(6)}
print(phonebook['Ellis'])
print(squares)
# collections.orderedDict
# Запоминает порядок вставки ключей
import collections
d = collections.OrderedDict(one=1, two=2, three=3)
print(d)
d['four'] = 4
print(d)
print(d.keys())  
# collections.defaultdict
# Возвращает значения, заданные по умолчанию для отсутствующих ключей
from collections import defaultdict
dd = defaultdict(list)  # Возвращает переданную по умолчанию фабрику
dd['dogs'].append('Rufus')
dd['dogs'].append('Katherine')
print(dd['cats'])
print(dd['dogs'])
# collections.ChainMap
# Группирует словари в таблицу соответствия
from collections import ChainMap
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)
print(chain)
print(chain['three'])  # ищет во всей цепочке
print(chain['one'])
# types.MappingProxyType
# Обертка словаря допускающая только его чтение
from types import MappingProxyType
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
print(read_only['one'])  # Позволяет только читать
writable['one'] = 42
print(read_only)
# Массивоподобные структуры данных
# list - изменяемые динамические
arr = ['один', 'два', 'три']
print(arr[0])
# Списки имеют хороший метод repr:
print(arr)
# Списки могут изменяться:
arr[1] = 'привет'
print(arr)
del arr[1]
print(arr)
# Списки могут содержать произвольные типы данных:
arr.append(23)
print(arr)
# tuple - неизменяемые
arr = 'один', 'два', 'три'
print(arr[0])
# Кортежи имеют хороший метод repr:
print(arr)
# Кортежи не могут изменяться:
#arr[1] = 'привет' TypeError: 'tuple' object does not support item assignment
#del arr[1] TypeError: 'tuple' object doesn't support item deletion
# Кортежи могут содержать произвольные типы данных:
# (При добавлении элементов создается копия кортежа)
arr + (23,)
print(arr)
# array.array - элементарные типизорванные массивы
import array
arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])
print(arr)
arr[1] = 23.0
print(arr)
del arr[1]
print(arr)
arr.append(42.0)
print(arr)
#arr[1] = 'Hello'  # TypeError: must be real number, not str
# str - незименяемые массивы символов unicode
arr = 'abcd'
print(arr[1])
print(arr)
#arr[1] = 'e'  # TypeError: 'str' object does not support item assignment
print(list(arr))
# bytes - неизменяемый массив одиночных байтов
arr = bytes((0, 1, 2, 3))
print(arr[1])
print(arr)
arr = b'x00x01x02x03'
print(arr)
#arr = bytes((0, 300))  # ValueError: bytes must be in range(0, 256)
#arr[1] = 23  # TypeError: 'bytes' object does not support item assignment
#del arr[1]  # TypeError: 'bytes' object doesn't support item deletion
# bytearray - изменяемый массив одиночных байтов
arr = bytearray((0, 1, 2, 3))
print(arr[1])
print(arr)
arr[1] = 23
print(arr)
print(arr[1])
del arr[1]
print(arr)
arr.append(42)
print(arr)
#arr = bytes((0, 300))  # ValueError: bytes must be in range(0, 256)
#arr[1] = 'Hello'  # TypeError: 'str' object cannot be interpreted as an integer
# Записи, структуры и объекты переноса данных
# dict
car1 = {
    'color': 'red',
    'mileage': 3381.2,
    'automate': True,
}
car2 = {
    'color': 'blue',
    'mileage': 12500,
    'automate': False,
}
print(car2)
print(car1['mileage'])
car2['mileage'] = 150
car2['front window'] = 'broken'
print(car2)
# tuple
car1 = ('red', 3812.4, True)
car2 = ('blue', 12344, False)
print(car1)
print(car2)
print(car2[1])
#car2[1] = 150  # TypeError: 'tuple' object does not support item assignment
# collections.namedtuple
from collections import namedtuple
p1 = namedtuple('Point', 'x y z')(1, 2, 3)
print(p1)
# typing.NamedTuple
from typing import NamedTuple
class Car(NamedTuple):
    color: str
    mileage: int
    automate: bool
car1 = Car('red', 3812.4, True)
print(car1)
#car1.mileage = 12  # AttributeError: can't set attribute
#car1.front_window = 'broken'  # AttributeError: 'Car' object has no attribute 'front_window' and no __dict__ for setting new attributes
# struct.Struct - Для упаковки данных для передачи по сети
# Множества и мультимножества тип bag
# set
vowels = {'a', 'o', 'e', 'i', 'y', 'g', 'g', 'd', 'z'}
print('e' in vowels)
letters = set('Alice')
print(letters.intersection(vowels))
vowels.add('x')
print(vowels)
# frozenset - неизменяемые множества
# Могут использоваться в качестве ключей словаря или элементами другого множества
vowels = frozenset({'a', 'o', 'e', 'i', 'y', 'g', 'g', 'd', 'z'})
#vowels.add('p')  # AttributeError: 'frozenset' object has no attribute 'add'
print(vowels)
d = {frozenset({1, 2, 3}): 'Hello'}
print(d[frozenset({1, 2, 3})])
# collections.Counter - мультимножество / мешок
# Допускает неоднократное появления объекта в множестве
from collections import Counter
inventory = Counter()
loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
print(inventory)
more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
print(inventory)
print(len(inventory))  # Возвращает кол-во уникальных элементов
print(sum(inventory.values()))  # Возвращает общее кол-во элементов
# Стеки с дисциплиной LIFO ( Last in, first out )
# collections.deque
from collections import deque
s = deque()
s.append('eat')
s.append('sleep')
s.append('programm')
print(s.pop())
print(s.pop())
print(s.pop())
#print(s.pop())  # IndexError: pop from an empty deque
# deque.LifoQueue
from queue import LifoQueue
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('programm')
print(s.get())
print(s.get())
print(s.get())
#print(s.get_nowait())  #  _queue.Empty
# Очереди FIFO ( First in, first out)
# collections.deque
# Реализована как двусторонний список, так что подходит для LIFO и FIFO
q = deque()
q.append('eat')
q.append('sleep')
q.append('programm')
print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())
#print(q.popleft())  # IndexError: pop from an empty deque
# queue.Queue
from queue import Queue
s = Queue()
s.put('eat')
s.put('sleep')
s.put('programm')
print(s.get())
print(s.get())
print(s.get())
# print(s.get_nowait())  # _queue.Empty
# multiprocessing.Queue
# Очередь совместных заданий
from multiprocessing import Queue
q = Queue()
q.put('eat')
print(q.get())
# Очереди с приоритетом
# Первее берет элемент с более большим "весом"
# list
q = []
q.append((2, 'program'))
q.append((1, 'eat'))
q.append((3, 'sleep'))
q.sort(reverse=True)
while q:
    next_item = q.pop()
    print(next_item)
# heapq
import heapq
q = []
heapq.heappush(q, (2, 'program'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))
while q:
    next_item = heapq.heappop(q)
    print(next_item)
# queue.PriorityQueue
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'program'))
q.put((1, 'eat'))
q.put((3, 'sleep'))
while not q.empty():
    next_item = q.get()
    print(next_item)