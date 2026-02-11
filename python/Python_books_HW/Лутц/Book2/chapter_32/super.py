#Traditional
class C:
    def act(self) : print('spam')
class D(C):
    def act(self):
        C.act(self)
        print('eggs')
x = D()
x.act()
#Using super
class C:
    def act(self) : print('spam')
class D(C):
    def act(self):
        super().act()
        print('eggs')
x = D()
x.act()
print('-' * 50)
#Trouble:
class A:
    def act(self) : print('A')
class B:
    def act(self) : print('B')
class C(A):
    def act(self): super().act()
x = C()
x.act()
class C(B, A):
    def act(self): super().act()
x = C()
x.act() #Только B
#Changing superclasses
class X:
    def m(self) : print('X.m')
class Y:
    def m(self) : print('Y.m')
class C(X):
    def m(self) : super().m()
i = C()
i.m()
C.__bases__ = (Y,)
i.m()
#MRO-super
class A:
    def __init__(self) : print('A.__init__')
class B(A):
    def __init__(self) : print('B.__init__'); A.__init__(self)
class C(A):
    def __init__(self) : print('C.__init__'); A.__init__(self)
x = B()
x = C()
print('-' * 50)
class D(B, C): pass
x = D()
class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
print('-' * 50)
x = D() #A - выполняется два раза
class A:
    def __init__(self) : print('A.__init__')
class B(A):
    def __init__(self) : print('B.__init__'); super().__init__()
class C(A):
    def __init__(self) : print('C.__init__'); super().__init__()
class D(B, C): pass
print('-' * 50)
x = D()