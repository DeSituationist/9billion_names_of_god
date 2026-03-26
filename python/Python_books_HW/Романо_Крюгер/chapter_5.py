# map
print(list(map(lambda *a: a, range(3))))
print(list(map(lambda *a: a, range(3), 'abc')))
print(list(map(lambda *a: a, range(3), 'abc', range(4, 7))))
students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]
def decorate(student):
    # создаем кортеж из двух элементов: суммы баллов по предметам
    # и данных о студенте
    return (sum(student["credits"].values()), student)
def undecorate(decorated_student):
    # отбрасываем сумму баллов, возвращаем только данные студента
    return decorated_student[1]['id']
print(students[0])
print(decorate(students[0]))
students = sorted(map(decorate, students), reverse=True)
students = list(map(undecorate, students))
print(students)
# zip
grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]
print(list(zip(avgs, grades)))
print(list(map(lambda *a: a, avgs, grades)))
# filter
test = [2, 5, 8, 0, 0, 1, 0]
print(list(filter(None, test)))
print(list(filter(lambda x: x, test)))
print(list(filter(lambda x: x > 4, test)))
# list comprehensions
squares = []
for n in range(10):
    squares.append(n ** 2)
print(squares)
squares = list(map(lambda n: n ** 2, range(10)))
print(squares)
print([n ** 2 for n in range(10)])
sq = [n ** 2 for n in range(10) if not n % 2]
print(sq)
items = 'ABCD'
pairs = [
    (items[a], items[b])
    for a in range(len(items))
    for b in range(a, len(items))
]
print(pairs)
mx = 10
import math
triples = [
    (a, b, int(c))
    for a in range(1, mx)
    for b in range(1, mx)
    if (c:=math.sqrt(a ** 2 + b ** 2)).is_integer()
]
print(triples)
# dict comprehensions
from string import ascii_lowercase
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap)
# set comprehensions
word = 'Hello'
letters1 = {c for c in word}
letters2 = set(c for c in word)
print(letters1, letters2)
# function-generator
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2
print(list(get_squares_gen(10)))
# send()
stop = False
def counter(start = 0):
    n = start
    while not stop:
        yield n
        n += 1
c = counter()
print(next(c))
print(next(c))
# stop = True
# print(next(c))  StopIteration
def counter(start=0):
    n = start
    while True:
        result = yield n # A
        print(type(result), result) # Б
        if result == "Q":
            break
        n += 1
c = counter()
print(next(c)) 
print(c.send("Wow!")) 
print(next(c)) 
# print(c.send("Q"))  StopIteration
# yield from
def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end))
for n in print_squares(2, 5):
    print(n)
# expression-generator
cubes_gen = (k ** 3 for k in range(10))
print(cubes_gen)
print(list(cubes_gen))