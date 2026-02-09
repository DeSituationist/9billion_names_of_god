class Wrapper:
    def __init__(self, object) : self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)
x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapped)
x = Wrapper({'a': 1, 'b': 2})
print(list(x.keys()))