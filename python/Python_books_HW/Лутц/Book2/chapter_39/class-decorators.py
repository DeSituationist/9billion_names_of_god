print('-'*30 + 'EXAMPLE-1' + '-'*30)
instances = {}
def singleton(aClass):
    def onCall(*args, **kwargs):
        if aClass not in instances:
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall
@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
@singleton
class Spam:
    def __init__(self, val):
        self.attr = val
bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())
sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())
x = Spam(val=42)
y = Spam(99)
print(x.attr, y.attr)
print('-'*30 + 'EXAMPLE-2' + '-'*30)
def singleton(aClass):
    instances = None
    def onCall(*args, **kwargs):
        nonlocal instances
        if instances == None:
            instances = aClass(*args, **kwargs)
        return instances
    return onCall
@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
@singleton
class Spam:
    def __init__(self, val):
        self.attr = val
bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())
sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())
x = Spam(val=42)
y = Spam(99)
print(x.attr, y.attr)
print('-'*30 + 'EXAMPLE-3' + '-'*30)
class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace: ', attrname)
        return getattr(self.wrapped, attrname)
x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapped)
x = Wrapper({'a': 1, 'b': 2})
print(list(x.keys()))
print('-'*30 + 'EXAMPLE-4' + '-'*30)
def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)
        def __getattr__(self, attrname):
            print('Trace: ', attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper
@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)
@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
food = Spam()
food.display()
print([food.fetches])
bob = Person('Bob', 40, 50)
print(bob.name)
print(bob.pay())
sue = Person('Sue', rate = 100, hours = 60)
print(sue.name)
print(sue.pay())
print(bob.name)
print(bob.pay())
print([bob.fetches, sue.fetches])

