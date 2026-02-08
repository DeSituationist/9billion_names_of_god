class Super:
    def hello(self):
        self.data1 = 'spam'
class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'
x = Sub()
print(x.__dict__)
print(x.__class__)
print(Sub.__bases__)
print(Super.__bases__)
y = Sub()
x.hello() # дополняет пространство имен данного экземляра, а не класса и не других экземляров
print(x.__dict__)
x.hola()
print(x.__dict__)
print(list(Sub.__dict__.keys()))
print(list(Super.__dict__.keys()))
print(y.__dict__)
x.data3 = 'toast'
x.__dict__['data3'] = 'ham'
print(x.__dict__)
print(list(name for name in dir(x) if not name.startswith('__')))
print(list(name for name in dir(y) if not name.startswith('__')))
print(list(name for name in dir(Sub) if not name.startswith('__')))
print(list(name for name in dir(Super) if not name.startswith('__')))