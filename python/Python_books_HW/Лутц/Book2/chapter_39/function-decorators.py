print('-'*30 + 'EXAMPLE-1' + '-'*30)
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call {} to {}'.format(self.calls, self.func.__name__))
        self.func(*args)
@tracer
def spam(a, b, c):
    print(a + b + c)
spam(1, 2, 3)
spam('a', 'b', 'c')
print('-'*30 + 'EXAMPLE-2' + '-'*30)
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call {} to {}'.format(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
@tracer
def spam(a, b, c):
    return a + b + c
@tracer
def eggs(x, y):
    print(x ** y)
spam(1, 2, 3)
spam(a = 4, b = 5, c = 6)
eggs(2, 16)
eggs(4, y = 4)
print('-'*30 + 'EXAMPLE-3' + '-'*30)
calls = 0
def tracer(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print('call {} to {}'.format(calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper
@tracer
def spam(a, b, c):
    print(a + b + c)
@tracer
def eggs(x, y):
    print(x ** y)
spam(1, 2, 3)
spam(a = 4, b = 5, c = 6)
eggs(2, 16)
eggs(4, y = 4)
print('-'*30 + 'EXAMPLE-4' + '-'*30)
def tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call {} to {}'.format(calls, func.__name__))
        return func(*args, **kwargs)
    return onCall
@tracer
def spam(a, b, c):
    print(a + b + c)
@tracer 
def eggs(N):
    return 2 ** N
spam(1, 2, 3)
spam(a = 4, b = 5, c = 6)
print(eggs(32))
class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    @tracer
    def lastName(self):
        return self.name.split()[-1]
print('methods...')
bob = Person('Bob Smith', 50000)
sue = Person('Sue Johnes', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(int(sue.pay))
print(bob.lastName(), sue.lastName())
print('-'*30 + 'EXAMPLE-4' + '-'*30)
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('calls {} to {}'.format(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):
        return wrapper(self, instance)
class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)
@tracer
def spam(a, b, c):
    print(a + b + c)
class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    @tracer
    def lastName(self):
        return self.name.split()[-1]
spam(1, 2, 3)
spam(a = 4, b = 5, c = 6)
bob = Person('Bob Smith', 50000)
sue = Person('Sue Johnes', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(int(sue.pay))
print(bob.lastName(), sue.lastName())