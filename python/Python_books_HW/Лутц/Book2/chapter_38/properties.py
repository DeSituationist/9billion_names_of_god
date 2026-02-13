class Person:
    def __init__(self, name): self._name = name
    def getName(self):
        print('fetch..')
        return self._name
    def setName(self, value):
        print('change..')
        self._name = value
    def delName(self):
        print('remove..')
        del self._name
    name = property(getName, setName, delName, 'name property docs')
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-'*30 + 'EXAMPLE-2' + '-'*30)
class PropSquare:
    def __init__(self, start):
        self.value = start
    def getX(self):
        return self.value ** 2
    def setX(self, value):
        self.value = value
    x = property(getX, setX)
p = PropSquare(3)
q = PropSquare(32)
print(p.x)
p.x = 4
print(p.x)
print(q.x)
