class ParentClass:
    def __init__(self):
        self.a = 1
        print('Parent class object created')
    def someMethod(self):
        print('Hello')
class ChildClass(ParentClass):
    def __init__(self):
        print('Child class object created')
parent = ParentClass()
child = ChildClass()
print(isinstance(parent, ParentClass))
print(isinstance(5, int))
print(isinstance(child, ParentClass))
print(isinstance(parent, (ParentClass, int))) #Один из типов в кортеже
print(isinstance(parent, ChildClass))
print(issubclass(ChildClass, ParentClass))
print(issubclass(ParentClass, ParentClass))
print(issubclass(ChildClass, int))
print(issubclass(ChildClass, (int, ParentClass)))
print(hasattr(parent, 'a'))
print(hasattr(parent, 'someMethod'))
hasattr(parent, 'b')