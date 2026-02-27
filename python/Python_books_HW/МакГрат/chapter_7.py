class Bird():
    '''Base class, describes bird properties'''
    count = 0
    def __init__(self, chat):
        self.sound = chat
        Bird.count += 1
    def talk(self):
        return self.sound
print('Class instances of:', Bird.__doc__)
polly = Bird('Squawk, squawk!')
print('number of birds:', polly.count)
print('polly says:', polly.talk())
harry = Bird('Tweet, tweet!')
print('Number of birds:', harry.count)
print('Harry says:', harry.talk())
chick = Bird('Cheep, cheep!')
chick.age = '1 week'
print('Chick says:', chick.talk())
print('Chick age:', chick.age)
chick.age = '2 weeks'
print('Chick now', chick.age)
setattr(chick, 'age', '3 weeks')
print('Chick attrs:')
for attrib in dir(chick):
    if not attrib.startswith('__'): print(attrib, ':', getattr(chick, attrib))
zola = Bird('Beep, beep')
print('Built-in instance attrs:')
for attrib in dir(zola): print(attrib) if attrib.startswith('__') else None
print('Class dict:')
for item in Bird.__dict__: print(item, ':', Bird.__dict__[item])
print('Instance dictionary:')
for item in zola.__dict__: print(item, ':', zola.__dict__[item])
class Songbird():
    def __init__(self, name, song):
        self.name = name
        self.song = song
        print(self.name, 'Is born')
    def sing(self):
        print(self.name, 'Sings:', self.song)
    def __del__(self):
        print(self.name, 'flew away!')
bird_1 = Songbird('Koko', 'Tweet, tweet')
print(bird_1.name, 'ID:', id(bird_1))
bird_1.sing()
del bird_1
bird_2 = Songbird('Louie', 'Chirp, chirp!')
print(bird_2.name, 'ID:', id(bird_2))
bird_2.sing()
bird_3 = Songbird('Misty', 'Squawk, squawk')
print(bird_3.name, 'ID:', id(bird_3))
del bird_2
del bird_3
class Polygon():
    width = 0
    height = 0
    def set_values(self, width, height):
        Polygon.width = width
        Polygon.height = height
class Rectangle(Polygon):
    def area(self):
        return self.width * self.height
class Triangle(Polygon):
    def area(self):
        return (self.height * self.width) / 2
rect = Rectangle()
trey = Triangle()
rect.set_values(4, 5)
trey.set_values(4, 5)
print('Rectangle area:', rect.area())
print('Triangle area:', trey.area())
class Person():
    '''Base class'''
    def __init__(self, name):
        self.name = name
    def speak(self, msg='(Calling base class)'):
        print(self.name, msg)
class Man(Person):
    '''Child class'''
    def speak(self, msg):
        print(self.name, ':\tHello!', msg)
class Hombre(Person):
    def speak(self, msg):
        print(self.name, '\tHola', msg)
guy_1 = Man('Richard')
guy_2 = Hombre('Ricardo')
guy_1.speak('Its a beautiful evening')
guy_2.speak('Es una tarde hermosa')
Person.speak(guy_1)
Person.speak(guy_2)
class Duck:
    def talk(self):
        print('Duck says: Quack!')
    def coat(self):
        print('Duck wears: Feathers')
class Mouse:
    def talk(self):
        print('Mouse says: Squeak!')
    def coat(self):
        print('Mouse wears: Fur')
def describe(object):
    object.talk()
    object.coat()
donald = Duck()
mickey = Mouse()
describe(donald)
describe(mickey)