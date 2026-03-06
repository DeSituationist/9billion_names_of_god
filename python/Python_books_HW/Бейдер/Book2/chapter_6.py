# цикл for
emails = {
    'Bob': 'bob@example.com',
    'Alice': 'alice@example.com',
}
for name, email in emails.items():
    print(f'{name} -> {email}')
# включения в списки
squares = [x * x for x in range(10)]
print(squares)
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)
# включение в множество
print({x * x for x in range(-9, 10)})
# включение в словарь
print({x: x * x for x in range(5)})
# нарезка
lst = [1, 2, 3, 4, 5]
del lst[:]
print(lst)  # Очистка списка / можно использовать lst.clear()
# Итераторы
class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return RepeaterIterator(self)
class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    def __next__(self):
        return self.source.value
repeater = Repeater('Hello')
for i, val in enumerate(repeater):
    if i > 10: break
    print(i, val)
class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value
repeater = Repeater('Hello')
for i, val in enumerate(repeater):
    if i > 5: break
    print(i, val)
# Ограниченный итератор
class BoundedRepeater:
    def __init__(self, value, max_repeaters):
        self.value = value
        self.max_repeaters = max_repeaters
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.max_repeaters:
            raise StopIteration
        self.count += 1
        return self.value
repeater = BoundedRepeater('hello', 3)
for it in repeater: print(it)
repeater = BoundedRepeater('Whats up', 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        print('Got StopIteration')
        break
    print(item)
# Генераторы
def repeater(value):
    while True: yield value  # Бесконечный генератор
rep = repeater('Hey')
print(rep)
print(next(rep))
# Генераторы с ограничением
def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value
for x in bounded_repeater('Привет', 4):
    print(x)
def bounded_repeater(value, max_repeats):
    for _ in range(max_repeats):
        yield value
# Выражения генераторы
iterator = ('Hello' for i in range(3))
for x in iterator:
    print(x)
# Выражения генераторы с фильтром
even_squares = (x * x for x in range(10) if x % 2 == 0)
for x in even_squares:
    print(x)
for x in ('Yo' for _ in range(3)): print(x)
# Цепочки итераторов
def integers():  # Генератор чисел
    for i in range(1, 9):
        yield i
def squared(seq):  # Генератор квадратов чисел
    for i in seq:
        yield i * i
chain = squared(integers())  # Цепочка генераторов
print(list(chain))
def negated(seq):  # Генератор отрицательных чисел
    for i in seq:
        yield -i
chain = negated(squared(integers()))  # Цепочка генераторов
print(list(chain))
# Сокращенная версия генераторов
integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)
print(list(negated))