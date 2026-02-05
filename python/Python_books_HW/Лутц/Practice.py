"""
#Part_2_practice
print("Task1")
print("---Ints---")
print(2**16)
print(2 / 5, 2 / 5.0)
print("---Strs---")
print("spam" + "eggs")
S = "ham"
print("eggs " + S)
print(S * 5)
print(S[:0])
print("green %s and %s" % ("eggs", S))
print("green {0} and {1}".format('eggs', S))
print("---Tuples---")
print(('x',)[0])
print(('x', 'y')[1])
print("---Lists---")
L = [1, 2, 3] + [4, 5, 6]
print(L, L[:], L[:0], L[-2], L[-2:])
print(([1, 2, 3] + [4, 5, 6])[2:4])
print([L[2], L[3]])
print(L.reverse(), L)
print(L.sort(), L)
print(L.index(4))
print("---Dicts---")
print({'a': 1, 'b': 2}['b'])
D = {'x': 1, 'y': 2, 'z': 3}
D['w'] = 0
print(D['x'] + D['w'])
D[(1, 2, 3)] = 4
print(list(D.keys()), list(D.values()), ((1, 2, 3) in D))
print([[]], ["", (), {}, None])
print("\nTask2\n")
L = [0, 1, 2, 3]
#print(L[4]) error
print(L[-1000:100])
x = L[3:1]
print(x)
print("\nTask3\n")
L = [0, 1, 2, 3]
L[2] = []
print(L)
L[2:3] = []
print(L)
del L[0]
print(L)
del L[1:]
print(L)
#L[1:2] = 1 error
print(L)
print("\nTask4\n")
X = 'spam'
Y = 'eggs'
X, Y = Y, X
print(X, Y)
print("\nTask5\n")
D = {}
D[1] = 'a'
D[2] = 'b'
print(D)
print("\nTask6\n")
keys = ['a', 'b', 'c']
values = [1, 2, 3]
D = dict(zip(keys, values))
#print(D['d']) error
D['d'] = 'spam'
print(D)
print("\nTask7\n")
#print([1, 2, 3] + '123', [1, 3, 4] + (1, 2, 3)) error
#print([1, 2, 3] + {'a': 1, 'b' :2}) error
print([1, 2, 3].append(1))
#print('123'.append('123')) error
#print([1, 2, 3].keys()) error
print("\nTask8\n")
S = "spam"
print(S[0][0][0][0][0])
S = list(S)
print(S[0][0][0][0][0])
print("\nTask9\n")
S = "spam"
S = S[:1] + 'l' + S[2:]
print(S)
#S[1] = 'l' error
print(S)
print("\nTask10\n")
PersonalData = {}
PersonalData['FIO'] = {'Name': 'Ilya', 'Surname': 'Volokh', 'Fathers Name': 'Olegovich'}
PersonalData['Age'] = 21
PersonalData['WorkPlace'] = 'LETI UNIVERSITY'
PersonalData['Address'] = 'Lunacharskogo'
print(PersonalData)
for key, value in PersonalData.items():
    print("{} = {}".format(key, value))
print("\nTask11\n")
myfile = open("myfile.txt", 'w+')
myfile.write("Hello file world!")
myfile.close()
readfile = open("myfile.txt", 'r')
line = readfile.readline()
print(line)
myfile.close()

#Part_3_practice
print("\nTask1\n")
S = "spam"
for x in S: print(ord(x), end = ' ')
sum = 0
for x in S: sum += ord(x)
print(sum)
print(map(ord, S))
print([ord(x) for x in S])
print("\nTask2\n")
for i in range(50):
    print('hello %d\n\a' % i)
print("\nTask3\n")
D = dict(a=1, b=2, c=3, d=100, e=45)
print(sorted(D.values()))
print("\nTask4\n")
L = [2 ** x for x in range(7)]
print(L)
X = 5
found = False
i = 0
if 2 ** X in L:
    print('at index', L.index(2**X))
else:
    print(X, 'not found')
"""
#Part_4_practice
print("\nTask1\n")
def printer(x) : print(x)
printer('str')
printer(3)
printer([1, 2, 3])
printer({'a': 1, 'b': 2})
#printer()     error 
#printer(1, [1, 2, 3])    error
print("\nTask2\n")
def adder(x, y) : return x + y
adder([1, 2, 3], [1, 2, 3])
adder('123', '123')
adder(3.4, 4.3)
print("\nTask3\n")
from functools import reduce
def adder(*args) : return reduce(lambda x, y: x + y, args)
adder(1, 2, 3, 4, 5)
adder('1', '2', '3')
adder(3.4, 4.3, 1, 5.3)
#print(adder({'a': 1, 'b': 2}, {'c': 3, 'd': 4})) error
print("\nTask4\n")
def adder(good="shovel", bad="gun", ugly="money") : return good + bad + ugly
print(adder('digging'))
print(adder('digging', 'looking'))
print(adder('digging', 'looking', 'killing'))
#print(adder('digging', 'looking', 'killing', 'running')) error
print(adder(ugly='1', good='2'))
def adder(**kwargs) : return reduce(lambda x, y: x + y, kwargs.values())
print(adder(good=1, bad=2, ugly=3))
print("\nTask5\n")
def copyDict(dict) : return {x : dict[x] for x in dict.keys()}
D = {'a': 1, 'b': 2}
print(copyDict(D))
print("\nTask6\n")
def addDict(dict1, dict2) : return {**dict1, **dict2}
D, D2 = {'a': 1, 'b': 2}, {'c': 3, 'd': 4} 
print(addDict(D, D2))
print("\nTask7\n")
def f1(a, b) : print(a, b)
def f2(a, *b) : print(a, b)
def f3(a, **b) : print(a, b)
def f4(a, *b, **c) : print(a, b, c)
def f5(a, b=2, c=3) : print(a, b, c)
def f6(a, b=2, *c) : print(a, b, c)
f1(1, 2)
f1(b=2, a=1)
f2(1, 2, 3)
f3(1, x=2, y=3)
f4(1, 2, 3, x=2, y=3)
f5(1)
f5(1, 4)
f6(1)
f6(1, 4)
print("\nTask8\n")
def checkPrime(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')
checkPrime(13)
checkPrime(13.0)
checkPrime(15)
checkPrime(15.0)
print("\nTask9\n")
from math import sqrt
l = [2, 4, 9, 16, 25]
for i in l: print(sqrt(i), end=' ')
print('\n')
print(list(map(sqrt, l)))
print([sqrt(i) for i in l])
print(list((sqrt(i) for i in l)))
print("\nTask10\n")
print('too old')
print("\nTask11\n")
def countdown(x):
    print(x)
    return "stop" if x == 0 else countdown(x - 1)
print(countdown(5))
print("\nTask12\n")
def factorial(N):
    return reduce(lambda x, y: x * y, range(1, N + 1))
print(factorial(4))