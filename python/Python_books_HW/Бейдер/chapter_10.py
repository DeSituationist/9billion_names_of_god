class Dog:
    def __init__(self, name: str, age: int, coat_color: str):
        self.name = name
        self.age = age
        self.coat = coat_color
    def __str__(self):
        return f'My name is {self.name}, i am {self.age} years old and i have {self.coat} coat'
philo = Dog('Philo', 5, 'brown')
print(philo)
class Car:
    def __init__(self, color: str, milage: int):
        self.color = color
        self.milage = milage
    def __str__(self):
        return f'The {self.color} car has {self.milage:,} miles'
bl_car = Car('Blue', 20000)
rd_car = Car('Red', 30000)
print(bl_car)
print(rd_car)
class Dog:
    species = 'Canis familiaris'
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    def speak(self, sound):
        return f'{self.name} says {sound}'
class GoldenRetriever(Dog):
    def speak(self, sound = 'bark'):
        super().speak(sound)
class Rectangle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
class Square(Rectangle):
    def __init__(self, side_width):
        super().__init__(side_width, side_width)
sq = Square(5)
print(sq.area())
class Animal:
    def __init__(self, name: str, age: int, who: str):
        self.name = name
        self.age = age
        self.who = who
    def speak(self, sound):
        return f'{self.who} says {sound}'
    def eats(self, food):
        return f'{self.who} eats {food}'
    def __str__(self):
        return f'I am {self.who} my name is {self.name} and i am {self.age} years old'
class Cow(Animal):
    sound = 'Moo'
    def __init__(self, name: str, age: int):
        super().__init__(name, age, 'cow')
    def speak(self):
        return super().speak(Cow.sound)
    def eats(self):
        return super().eats('grass')
class Duck(Animal):
    sound = 'Quack'
    def __init__(self, name: str, age: int):
        super().__init__(name, age, 'duck')
    def speak(self):
        return super().speak(Duck.sound)
    def eats(self):
        return super().eats('mosquitos')
c_1 = Cow('c_Jerry', 5)
c_2 = Cow('c_Timothey', 8)
d_1 = Duck('d_Jerry', 1)
d_2 = Duck('d_Timothey', 2)
print(c_1)
print(c_2)
print(d_1)
print(d_2)
print(c_1.eats())
print(d_1.eats())
print(c_1.speak())
print(d_1.speak())