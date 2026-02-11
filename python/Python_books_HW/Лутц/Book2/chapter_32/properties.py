class properties():
    def getage(self) : return 40
    def setage(self, value): 
        print('set age: {}'.format(value))
        self._age = value
    age = property(getage, setage, None, None)
x = properties()
x.age = 42
print(x.age)
print(x._age)