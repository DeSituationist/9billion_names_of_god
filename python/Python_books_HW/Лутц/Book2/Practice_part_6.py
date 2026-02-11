print('-'*30 + 'TASK-1' + '-'*30)
'''
class Adder():
    def add(self, x, y): print('Not implemented')
class ListAdder():
    def add(x, y): return x + y
class DictAdder():
    def add(x, y): return {**x, **y}
x, y = [1, 4, 6], [2, 5, 7]
print(ListAdder.add(x, y))
x, y = {'a': 1, 'b': 3, 'c': 0}, {'a': 3, 'd': 4, 'e': 10}
print(DictAdder.add(x, y))
'''
class Adder():
    def __init__(self): self.data = []
    def __add__(self, other): self.add(other)
    def add(self, other): return self.data + other.data
class ListAdder(Adder) : pass
class DictAdder(Adder) : 
    def add(self, y): return {**self.data, **y.data}
x, y = ListAdder(), ListAdder()
x.data, y.data = [1, 2, 3], [4, 5, 6]
print(x.add(y))
x, y = DictAdder(), DictAdder()
x.data, y.data = {'a': 1, 'b': 3, 'c': 0}, {'a': 3, 'd': 4, 'e': 10}
print(x.add(y))
print('-'*30 + 'TASK-2' + '-'*30)
class MyList():
    def __init__(self) : self.data = []
    def __add__(self, other) : 
        if isinstance(other, MyList):
            return self.data + other.data
        else: 
            return self.data + other
    def __getitem__(self, index) : 
        if isinstance(index, int):
            return self.data[index]
        else: 
            return self.data[index.start:index.stop:index.step]
    def __iter__(self) : return iter(self.data)
    def append(self, item) : self.data.append(item)
    def sort(self) : return sorted(self.data)
x = MyList()
x.data = [6, 5, 3, 7]
y = MyList()
y.data = [1, 2, 3]
print(x + y)
y = [1, 2, 3, 4]
print(x + y)
print(x[1])
print(x[:])
print(x[0:-1:2])
print(x.sort())
x.append(2)
print(x.data)
z = x.__iter__()
print(next(z))
print(next(z))
print(next(z))
print(next(z))
#Через наследование от list
'''
class MyList(list):
    def __init__(self):
        super().__init__()
    def sort(self):
        return sorted(self)
x = MyList()
x.extend([6, 5, 3, 7])
print(x)
y = MyList()
y.extend([1, 2, 3])
print(y)
print(x + y)
y = [1, 2, 3, 4]
print(x + y)
print(x[1])
print(x[:])
print(x[0:-1:2])
print(x.sort())
x.append(2)
print(x)
z = x.__iter__()
print(next(z))
print(next(z))
print(next(z))
print(next(z))
'''
print('-'*30 + 'TASK-3' + '-'*30)
#У каждого экземпляра отдельный counter
class MyListSub(MyList):
    counter = 0
    def __add__(self, other):
        self.counter += 1
        print('Added something to list: {} times'.format(self.counter))
        return MyList.__add__(self, other)
x = MyListSub()
x.data = [6, 5, 3, 7]
y = MyListSub()
y.data = [1, 2, 3]
print(x + y)
z = [1, 2, 3, 4]
print(x + z)
print(type(x + z))
print(x.counter)
print(y.counter)
#У всех экземпляров общий counter
class MyListSub(MyList):
    counter = 0
    def __add__(self, other):
        MyListSub.counter += 1
        print('Added something to list: {} times'.format(MyListSub.counter))
        return MyList.__add__(self, other) # Возвращает объект класса list
x = MyListSub()
x.data = [6, 5, 3, 7]
y = MyListSub()
y.data = [1, 2, 3]
print(x + y)
z = [1, 2, 3, 4]
print(x + z)
print(type(x + z))
print(x.counter)
print(y.counter)
#Возвращает объект класса MyListSub
class MyListSub(MyList):
    counter = 0
    def __add__(self, other):
        new_list = MyListSub()
        MyListSub.counter += 1
        print('Added something to list: {} times'.format(MyListSub.counter))
        new_list.data = MyList.__add__(self, other) # Возвращает объект класса list
        return new_list
x = MyListSub()
x.data = [6, 5, 3, 7]
y = MyListSub()
y.data = [1, 2, 3]
print(x + y)
z = [1, 2, 3, 4]
c = x + z
print(c)
print(type(c))
print(x.counter)
print(y.counter)
print('-'*30 + 'TASK-4' + '-'*30) #Переделать
class Attrs:
    counter = 0
    def __init__(self) : 
        self.data = []
    def __getitem__(self, index) : 
        if isinstance(index, int):
            return self.data[index]
        else: 
            return self.data[index.start:index.stop:index.step]
    def __setitem__(self, index, value):
        Attrs.counter += 1
        if isinstance(index, int):
            self.data[index] = value
        else: 
            self.data[index.start:index.stop] = value
    def __getattribute__(self, name):
        print(f"Called attribute: {name}")
        return super().__getattribute__(name)
x = Attrs()
x.data = [1, 2, 3]
print(x[1])
x[1] = 42 
print(x.counter)
print('-'*30 + 'TASK-5' + '-'*30)
class Set(list):
    def __init__(self, value = []):
        list.__init__(self)
        self.concat(value)
    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)
    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res
    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)
    def __and__(self, other) : return self.intersect(other)
    def __or__(self, other) : return self.union(other)
    def __repr__(self) : return 'Set: ' + list.__repr__(self)
x = Set([1, 3, 5, 7])
y = Set([2, 1, 3, 4, 5, 6])
print(x, y, len(x))
print(x.intersect(y), y.union(x))
print(x & y, x | y)
x.reverse(); print(x)
print(x[2])
for i in x:
    print(i)
x = Set('123')
y = ''
print(x.intersect(y))
class SetSub(Set):
    def intersect(self, *args):
        base = self
        for i in args:
            base = Set.intersect(self, i)
        return base
x = SetSub([1, 3, 5, 7])
y = SetSub([2, 1, 3, 4, 5, 6])
z = SetSub([1, 3, 5])
print(x.intersect(y, z))
print(x)
print('-'*30 + 'TASK-6' + '-'*30)
class Lister:
    def __init__(self):
        self.res = ''
        self.offset = 0
    def first_listing(self, cls):
        self.res = self.res + str([cls.__name__] + [x for x in cls.__dict__ if not x.startswith('__')]) + '\n'
    def listing(self, cls):
        for supcls in cls.__bases__:
            self.offset +=2
            self.res += '--' * self.offset
            self.res = self.res + str([supcls.__name__] + [x for x in supcls.__dict__ if not x.startswith('__')]) + '\n'
            self.listing(supcls)
x = Lister()
x.first_listing(SetSub)
x.listing(SetSub)
print(x.res)
print('-'*30 + 'TASK-7' + '-'*30)
#Customer makes order
class LunchHouse:
    def __init__(self) :
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName): 
        self.customer.food = self.customer.placeOrder(foodName, self.employee)
        self.result()
    def result(self): 
        self.customer.printFood()
class Customer:
    def __init__(self) : 
        self.food = None
    def placeOrder(self, foodName, employee): return employee.takeOrder(foodName)
    def printFood(self): print(self.food.name)  
class Employee:
    def takeOrder(self, foodName): return Food(foodName)
class Food:
    def __init__(self, name) : self.name = name
x = LunchHouse()
x.order('Pizza')
#Employee takes order
class LunchHouse:
    def __init__(self) :
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName): 
        self.customer.food = self.employee.takeOrder(foodName)
        self.result()
    def result(self): 
        self.customer.printFood()
class Customer:
    def __init__(self): 
        self.food = None
    def printFood(self): print(self.food.name)  
class Employee:
    def takeOrder(self, foodName): return Food(foodName)
class Food:
    def __init__(self, name) : self.name = name
x = LunchHouse()
x.order('Pizza')
print('-'*30 + 'TASK-8' + '-'*30)
class Animal:
    def reply(self): self.speak()
class Mammal(Animal): 
    def speak(self): print('I am mammal')
class Cat(Mammal):
    def speak(self): print('I am cat')
class Dog(Mammal):
    def speak(self): print('I am dog')
class Primate(Mammal):
    def speak(self): print('I am Primate')
class Hacker(Primate): pass
spot = Cat()
spot.reply()
data = Hacker()
data.reply()
print('-'*30 + 'TASK-9' + '-'*30)
class Scene: 
    def __init__(self):
        self.customer = Cusomter()
        self.clerk = Clerk()
        self.parrot = Parrot()
    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()
class Cusomter: 
    def line(self): print('I am cutomer')
class Clerk:
    def line(self): print('I am clerk')
class Parrot:
    def line(self): print('I am parrot')
x = Scene()
x.action()