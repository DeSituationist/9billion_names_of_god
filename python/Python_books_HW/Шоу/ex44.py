'''
#Наследование
class Parent():
    def implicit(self):
        print('Parent\'s implicit()')
class Child(Parent):
    pass
dad = Parent()
son = Child()
dad.implicit()
son.implicit()
#Переопределение
class Parent():
    def override(self):
        print('Родительский override()')
class Child(Parent):
    def override(self):
        print('Потомок override()')
dad = Parent()
son = Child()
dad.override()
son.override()
#Дополнение
class Parent():
    def altered(self):
        print('Parents altered()')
class Child(Parent):
    def altered(self):
        print('Child, before parents altered()')
        super().altered()
        print('Child after parents altered()')
dad = Parent()
son = Child()
dad.altered()
son.altered()
'''
#Композиция
class Other():
    def override(self):
        print('Класс other override')
    def implicit(self):
        print('Class other implicit')
    def altered(self):
        print('class other altered')
class Child():
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print('Child override')
    def altered(self):
        print('Child before other altered call')
        self.other.altered()
        print('Child after other altered call')
son = Child()
son.implicit()
son.override()
son.altered()