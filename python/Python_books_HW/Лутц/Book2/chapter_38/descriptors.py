class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')
class Subject:
    attr = Descriptor()
x = Subject()
x.attr #Descriptor.__get__(Subject.attr, x, Subject)
class D:
    def __get__(*args) : print('get')
class C:
    a = D()
x = C()
x.a
C.a
x.a = 99
print(x.a)
y = C()
y.a
C.a
class D:
    def __get__(*args) : print('get')
    def __set__(*args) : raise AttributeError('cannot set') #Атрибут только для чтения
class C:
    a = D()
x = C()
x.a
#x.a = 99 error
print('-'*30 + 'EXAMPLE-1' + '-'*30)
'''
class Name:
    'name descriptor docs'
    def __get__(self, instance, owner): # self - экземпляр класса Name, instance - экземпляр класса Person, owner - класс Person
        print('fetch..')
        return instance._name
    def __set__(self, instance, value):
        print('change..')
        instance._name = value
    def __delete__(self, instance):
        print('remove..')
        del instance._name
class Person:
    def __init__(self, name):
        self._name = name
    name = Name()
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
'''
class Person:
    def __init__(self, name):
        self._name = name
    class Name:
        'name descriptor docs'
        def __get__(self, instance, owner): # self - экземпляр класса Name, instance - экземпляр класса Person, owner - класс Person
            print('fetch..')
            return instance._name
        def __set__(self, instance, value):
            print('change..')
            instance._name = value
        def __delete__(self, instance):
            print('remove..')
            del instance._name
    name = Name()
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print(Person.Name.__doc__)
print('-'*30 + 'EXAMPLE-2' + '-'*30)
class DescSquare:
    def __init__(self, start):
        self.value = start
    def __get__(self, instance, owner):
        return self.value ** 2
    def __set__(self, instance, value):
        self.value = value
class Client1:
    x = DescSquare(3)
class Client2:
    x = DescSquare(32)
c1 = Client1()
c2 = Client2()
print(c1.x)
c1.x = 4
print(c1.x)
print(c2.x)
print('-'*30 + 'EXAMPLE-3' + '-'*30)
class DescState:
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner):
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value):
        print('DescState set')
        self.value = value
class CalcAttrs:
    x = DescState(2)
    y = 3
    def __init__(self):
        self.z = 4
obj = CalcAttrs()
print(obj.x, obj.y, obj.z)
obj.x = 5
CalcAttrs.y = 6
obj.z = 7
print(obj.x, obj.y, obj.z)
obj2 = CalcAttrs()
print(obj2.x, obj2.y, obj2.z)
print('-'*30 + 'EXAMPLE-4' + '-'*30)
class InstState:
    def __get__(self, instance, owner):
        print('InstState get')
        return instance._x * 10
    def __set__(self, instance, value):
        print('InstState set')
        instance._x = value
class CalcAttrs:
    x = InstState()
    y = 3
    def __init__(self):
        self._x = 2
        self.z = 4
obj = CalcAttrs()
print(obj.x, obj.y, obj.z)
obj.x = 5
CalcAttrs.y = 6
obj.z = 7
print(obj.x, obj.y, obj.z)
obj2 = CalcAttrs()
print(obj2.x, obj2.y, obj2.z)
print('-'*30 + 'EXAMPLE-5' + '-'*30)
class DescBoth:
    def __init__(self, data):
        self.data = data
    def __get__(self, instance, owner):
        return '{}, {}'.format(self.data, instance.data)
    def __set__(self, instance, value):
        instance.data = value
class Client:
    def __init__(self, data):
        self.data = data
    managed = DescBoth('spam')
i = Client('eggs')
print(i.managed)
i.managed = 'SPAM'
print(i.data)
print(i.managed)
print('-'*30 + 'EXAMPLE-5-property-using-descriptor-class' + '-'*30)
class Property:
    def __init__(self, fget = None, fset = None, fdel = None, doc = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc
    def __get__(self, instance, instancetype= None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('cant get attribute')
        return self.fget(instance)
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('cant set attribute')
        self.fset(instance, value)
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('cant delete attribute')
        self.fdel(instance)
class Person:
    def getName(self): print('getName...')
    def setName(self, value): print('setName...')
    name = Property(getName, setName)
x = Person()
x.name
x.name = 'Bob'
#del x.name no delete func from Person class to Property