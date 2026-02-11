#Простой метод
class Spam:
    numInstances = 0
    def __init__(self): Spam.numInstances = Spam.numInstances + 1
    def printNumInstances(): print('Number of instances created: {}'.format(Spam.numInstances))
a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
#a.printNumInstances() error
class Methods:
    def imeth(self, x) : print([self, x])
    def smeth(x) : print([x])
    def cmeth(cls, x) : print([cls, x])
    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)
obj = Methods()
print(obj.imeth(1))
print(Methods.imeth(obj, 2))
print(Methods.smeth(4))
print(obj.smeth(4))
print(Methods.cmeth(5))
print(obj.cmeth(5))
print('-' * 50)
#Статический метод
class Spam:
    numInstances = 0
    def __init__(self): Spam.numInstances += 1
    def printNumInstances(): print('Number of instances created: {}'.format(Spam.numInstances))
    printNumInstances = staticmethod(printNumInstances)
a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
a.printNumInstances() #Также можно вызывать через любой экземпляр
class Sub(Spam):
    def printNumInstances():
        print('extra stuff...')
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)
a = Sub()
b = Sub()
c = Sub()
Sub.printNumInstances()
a.printNumInstances()
print('-' * 50)
#Метод класса
class Spam:
    numInstances = 0
    def __init__(self): Spam.numInstances += 1
    def printNumInstances(cls): print('Number of instances created: {}, {}'.format(cls.numInstances, cls))
    printNumInstances = classmethod(printNumInstances)
class Sub(Spam):
    def printNumInstances(cls):
        print('Extra stuff...', cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)
class Other(Spam): pass
x = Sub()
y = Spam()
z = Other()
x.printNumInstances()
Sub.printNumInstances()
y.printNumInstances()
z.printNumInstances()
print('-' * 50)
'''
Статичные методы - для подсчета по всем классам
Методы класса - для подсчета в каждом классе отдельно
'''
class Spam:
    numInstances = 0
    def count(cls) : cls.numInstances += 1
    def __init__(self) : self.count()
    count = classmethod(count)
class Sub(Spam):
    numInstances = 0
    def __init__(self) : Spam.__init__(self)
class Other(Spam): numInstances = 0
x1, x2, x3 = Sub(), Sub(), Sub()
y1, y2 = Spam(), Spam()
z = Other()
print('Of spam: {}; of Sub: {}; of Other: {}'.format(Spam.numInstances, Sub.numInstances, Other.numInstances))