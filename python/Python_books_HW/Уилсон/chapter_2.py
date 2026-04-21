import math
# Контракты: объект считается фигурой, только если в нем есть методы с этими именами
# и если они выполняют цель, описанную в своем имени.
class Shape:
    def __init__(self, name):
        self.name = name
    def perimeter(self):
        raise NotImplementedError('perimeter')
    def area(self):
        raise NotImplementedError('area')
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
    def perimeter(self):
        return 4 * self.side
    def area(self):
        return self.side * self.side
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2
# Полиморфизм / Утиная типизация ( полиморфизм включает наследование)
# Так как методы у классов одинаковые мы можем закрыть глаза на остальные различия
examples = [Square('sq', 3), Circle('ci', 2)]
for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    print(f'perimeter {n} equals {p:.2f}, and area - {a:.2f}')
# Псевдоним ( Алиас )
def example():
    print('Example called')
alias = example()

def square_perimeter(thing):
    return 4 * thing['side']
def square_area(thing):
    return thing['side'] ** 2
def square_new(name, side):
    return {
        'name': name,
        'side': side,
        'perimeter': square_perimeter,
        'area': square_area,
    }

def circle_perimeter(thing):
    return 2 * math.pi * thing['radius']
def circle_area(thing):
    return math.pi * thing['radius'] ** 2
def circle_new(name, radius):
    return {
        'name': name,
        'radius': radius,
        'perimeter': circle_perimeter,
        'area': circle_area,
    }

def call(thing, method_name):
    return thing[method_name](thing)
examples = [square_new('sq', 3), circle_new('ci', 2)]
# метод класса - функция, которая первым аргументом принимает self
for ex in examples:
    n = ex['name']
    p = call(ex, 'perimeter')
    a = call(ex, 'area')
    print(f'{n} {p:.2f} {a:.2f}')

Square = {
    'perimeter': square_perimeter,
    'area': square_area,
    '_classname': 'Square',
}
def square_new(name, side):
    return {
        'name': name,
        'side': side,
        '_class': Square,
    }

Circle = {
    'perimeter': circle_perimeter,
    'area': circle_area,
    '_classname': 'Circle',
}
def circle_new(name, radius):
    return {
        'name': name,
        'radius': radius,
        '_class': Circle,
    }

def call(thing, method_name):
    return thing['_class'][method_name](thing)

examples = [square_new('sq', 3), circle_new('ci', 2)]

for ex in examples:
    n = ex['name']
    p = call(ex, 'perimeter')
    a = call(ex, 'area')
    c = ex['_class']['_classname']
    print(f'{n} is a {c}: {p:.2f} {a:.2f}')

# args / kwargs
# varargs ( variable arguments ) Переменное кол-во элементов 
def show_args(title, *args, **kwargs):
    print(f'{title} args "{args}" and kwargs "{kwargs}"')

show_args('None')
show_args('One unnamed', 1)
show_args('One named', second = '2')
show_args('One for each', 3, four = '4')

# spread
# Распаковака аргументов

def show_spread(left, middle, right):
    print(f'left {left} middle {middle} right {right}')
all_in_list = [1, 2, 3]
show_spread(*all_in_list)
all_in_dict = {'right': 30, 'left': 10, 'middle': 20}
show_spread(**all_in_dict)

def square_larger(thing, size):
    return call(thing, 'area') > size

Square = {
    'perimeter': square_perimeter,
    'area': square_area,
    'larger': square_larger,
    '_classname': 'Square',
}

def circle_larger(thing, size):
    return call(thing, 'area') > size

Circle = {
    'perimter': circle_perimeter,
    'area': circle_area,
    'larger': circle_larger,
    '_classname': 'Circle',
}
def call(thing, method_name, *args):
    return thing['_class'][method_name](thing, *args)

examples = [square_new('sq', 3), circle_new('ci', 2)]

for ex in examples:
    result = call(ex, 'larger', 10)
    print(f'is {ex['name']} larger? {result}')
# Наследование
class Shape:
    def __init__(self, name):
        self.name = name
    def perimeter(self):
        raise NotImplementedError('perimeter')
    def area(self):
        raise NotImplementedError('area')
    def density(self, weight):
        return weight / self.area()
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
    def perimeter(self):
        return 4 * self.side
    def area(self):
        return self.side * self.side
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2
    
examples = [Square('sq', 3), Circle('ci', 2)]

for ex in examples:
    n = ex.name
    d = ex.density(5)
    print(f'{n}: {d:.2f}')

def shape_density(thing, weight):
    return weight / call(thing, 'area')
Shape = {
    'density': shape_density,
    '_classname': 'Shape',
    '_parent': None,
}
Square = {
    'perimeter': square_perimeter,
    'area': square_area,
    '_classname': 'Square',
    '_parent': Shape,
}
Circle = {
    'perimter': circle_perimeter,
    'area': circle_area,
    'larger': circle_larger,
    '_classname': 'Circle',
    '_parent': Shape,
}
def call(thing, method_name, *args):
    method = find(thing['_class'], method_name)
    return method(thing, *args)
def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls['_parent']
    raise NotImplementedError('method_name')

examples = [square_new('sq', 3), circle_new('ci', 2)]

for ex in examples:
    n = ex['name']
    d = call(ex, 'density', 5)
    print(f'{n}: {d:.2f}')
# Конструкторы чтобы объекты создавались правильно
def shape_new(name):
    return {
        'name': name,
        '_class': Shape,
    }
Shape = {
    'density': shape_density,
    '_classname': 'Shape',
    '_parent': None,
    '_new': shape_new,
}
def make(cls, *args): # Вызов родительского метода
    return cls['_new'](*args)
def square_new(name, side):
    return make(Shape, name) | {
        'side': side,
        '_class': Square,
    }
def circle_new(name, radius):
    return make(Shape, name) | {
        'radius': radius,
        '_class': Circle,
    }
Square = {
    'perimeter': square_perimeter,
    'area': square_area,
    '_classname': 'Square',
    '_parent': Shape,
    '_new': square_new,
}
Circle = {
    'perimter': circle_perimeter,
    'area': circle_area,
    'larger': circle_larger,
    '_classname': 'Circle',
    '_parent': Shape,
    '_new': circle_new,
}
examples  =[make(Square, 'sq', 3), make(Circle, 'ci', 2)]
for ex in examples:
    n = ex['name']
    d = call(ex, 'density', 5)
    print(f'{n}: {d:.2f}')