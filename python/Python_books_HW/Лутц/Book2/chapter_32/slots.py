class limiter(object):
    __slots__ = ['age', 'name', 'job'] #для избежания опечаток при обращении к атрибутам
x = limiter()
x.age = 40
print(x.age)
class C:
    __slots__ = ['a', 'b']
x = C()
x.a = 1
print(x.a)
#x.__dict__ no attribute 
getattr(x, 'a')
setattr(x, 'b', 2)
print(x.b)
print('a' in dir(x))
class D:
    __slots__ = ['a', 'b']
    def __init__(self) : self.d = 4
#x = D() object has no attribute d, атрибут не указан в slots
class D:
    __slots__ = ['a', 'b', '__dict__']
    c = 3
    def __init__(self) : 
        self.d = 4
x = D()
print(D.__dict__)
print(x.__dict__)
print(x.__slots__)
print(getattr(x, 'c'))
#Объединение slots через наследование
class E:
    __slots__ = ['c', 'd']
class D(E):
    __slots__ = ['a', '__dict__']
x = D()
x.a = 1; x.b = 2; x.c = 3
print(x.a, x.c)