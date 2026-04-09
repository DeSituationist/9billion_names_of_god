# Python — язык с динамической и строгой типизацией.
# Строгая типизация означает, что Python не выполняет неявные преобразования типов, которые могли бы привести к неожиданному поведению.
# Одновременно с этим Python — язык с динамической типизацией. Это означает, что тип переменной определяется во время выполнения и в коде его явно указывать не нужно.
# duck typing
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius**2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
def print_shape_info(shape):
    print(f'{shape.__class__.__name__} area: {shape.area()}')
circle = Circle(5)
rectangle = Rectangle(4, 6)
print_shape_info(circle)
print_shape_info(rectangle)
# function annotations
def greeter(name):
    return f'Hello, {name}!'
def greeter_annotated(name:str) -> str:
    return f'Hello, {name}'
from typing import Any
def reverse_any(items: list[Any]) -> list[Any]:
    return list(reversed(items))
def greeter(name: str = 'stranger') -> str:
    return f'Hello, {name}!'
from typing import Optional
def greeter_optional(name: Optional[str] = None) -> str:
    if name is not None:
        return f'Hello, {name}!'
    return 'No one to greet'
def connect_to_db(host: str, port: int | str): # | - or / или
    print(f'Connecting to {host} on port {port}')
# дженерики ( обобщенные типы )
def last[T](items: list[T]) -> T | None:
    return items[-1] if items else None
# Аннтоация переменных
x : int = 10
x : float = 3.14
x : bool = True
x : str = 'Hello'
x : bytes = b'Hello'
x : list[int] = [7, 14, 11]
x : set[int] = {1, 2, 3}
x : dict[str, float] = {'planck' : 6.26}
x : list[int | str] = [0, 1, 1, 2, 'fibonacci', 'rules']
a : tuple[int, ...] = (1, 2, 3) # бесконечное число типов
b : tuple[()] = () # пустой
# Аннотация с абстрактными классами
from collections.abc import Mapping, Sequence
def average_bad(v : list[float]) -> float:
    return sum(v) / len(v)
def average(v : Sequence[float]) -> float: # Через абстрактный класс последовательность
    return sum(v) / len(v)
from collections.abc import Iterable
def process_items(items: Iterable) -> None: # Так как только перебирает
    for item in items:
        print(item)
from collections.abc import Callable
def process_callback(arg: str, callback: Callable[[str], str]): # Принимает str и возвращает str
    return callback(arg)