class Catcher:
    def __getattr__(self, name):
        print('Get: ', name)
    def __setattr__(self, name, value):
        print('Set: ', name, ' ', value)
x = Catcher()
x.job
x.pay
x.pay = 99
print(dir(x))
print('-'*30 + 'EXAMPLE-1' + '-'*30)
class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname) #возварщает append от object 
x = Wrapper([1, 2, 3])
x.append(4) #в возвращенную функцию append передается 4
print(x.wrapped) 
'''
def __setattr__(self, name, value):
    super().__setattr__(self, 'other', value) - выход из цикла
def __getattribute__(self, name):
    super.__getattribute__(self, 'other') - выход из цикла
'''
print('-'*30 + 'EXAMPLE-2' + '-'*30)
class Person:
    def __init__(self, name):
        self.name = name
    def __getattr__(self, attr):
        print('get: ', attr)
        if attr == 'name':
            return self._name
        else:
            raise AttributeError(attr)
    def __setattr__(self, attr, value):
        print('set: ', attr)
        if attr == 'name':
            attr = '_name'
        self.__dict__[attr] = value
    def __delattr__(self, attr):
        print('del: ', attr)
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
#print(bob.name) error
print('-'*30 + 'EXAMPLE-3' + '-'*30)
class AttrSquare:
    def __init__(self, start):
        self.value = start
    def __getattr__(self, attr):
        if attr == 'x':
            return self.value ** 2
        else:
            raise AttributeError(attr)
    def __setattr__(self, attr, value):
        if attr == 'x':
            attr = 'value'
        self.__dict__[attr] = value
a = AttrSquare(3)
b = AttrSquare(32)
print(a.x)
a.x = 4
print(a.x)
print(b.x)
print('-'*30 + 'EXAMPLE-4-ALL-METHODS' + '-'*30)
print('-'*30 + 'EXAMPLE-4-1-property' + '-'*30)
class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)
    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)
x = Powers(3, 4)
print(x.square)
print(x.cube)
x.square = 5
print(x.square)
print('-'*30 + 'EXAMPLE-4-2-descriptor' + '-'*30)
class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value
class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3
class Powers:
    square = DescSquare()
    cube = DescCube()
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
x = Powers(3, 4)
print(x.square)
print(x.cube)
x.square = 5
print(x.square)
print('-'*30 + 'EXAMPLE-4-3-getattr' + '-'*30)
class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr: ', name)
    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value
x = Powers(3, 4)
print(x.square)
print(x.cube)
x.square = 5
print(x.square)