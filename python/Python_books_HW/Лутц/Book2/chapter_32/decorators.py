class Spam:
    numInstances = 0
    def __init__(self): Spam.numInstances += 1
    @staticmethod
    def printNumInstances(): print('Number of instances created: {}'.format(Spam.numInstances))
a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
a.printNumInstances()
print('-' * 50)
class Methods:
    def imeth(self, x) : print([self, x])
    @staticmethod
    def smeth(x) : print([x])
    @classmethod
    def cmeth(cls, x) : print([cls, x])
    @property
    def name(self) : return 'Bob ' + self.__class__.__name__
obj = Methods()
print(obj.imeth(1))
print(Methods.imeth(obj, 2))
print(Methods.smeth(4))
print(obj.smeth(4))
print(Methods.cmeth(5))
print(obj.cmeth(5))
print(obj.name)
print('-' * 20 + 'FUNCTION DECORATORS' + '-' * 20)
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call from {} to {}'.format(self.calls, self.func.__name__))
        return self.func(*args)
@tracer
def spam(a, b, c): return a + b + c
print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))