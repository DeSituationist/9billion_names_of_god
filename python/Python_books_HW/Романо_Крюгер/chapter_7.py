# exceptions
def squareroot(number):
    if number < 0:
        raise ValueError('No negative nubmers please')
    return number ** 0.5
def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    return (- b - squareroot(d) / (2 * a), - b + squareroot(d) / (2 * a))
# print(quadratic(1, 0, 1)) ValueError: No negative nubmers please
def try_syntax(numerator, denominator):
    try:
        print(f'in the try block: {numerator}/{denominator}')
        result = numerator / denominator
    except (ZeroDivisionError, TypeError) as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')
print(try_syntax(12, 4))
print(try_syntax(11, 0))
# class (Exception)
class NotFoundError(Exception):
    pass
vowels = dict(a=1, e=5, i=9, o=15, u=21)
'''
Traceback (most recent call last):
  File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 30, in <module>
    raise NotFoundError(*e.args) from None
NotFoundError: y

try:
    pos = vowels['y']
except KeyError as e:
    raise NotFoundError(*e.args) from None
'''
def validate_age(age):
    if not isinstance(age, int): raise TypeError(f'Not an integer {age}')
    if age < 0: raise ValueError(f'Negative age: {age}')
def validate_ages(ages):
    errors = []
    for age in ages:
        try:
            validate_age(age)
        except Exception as e:
            errors.append(e)
    if errors: raise ExceptionGroup('Validation errors', errors)
'''
validate_ages([24, -5, 'ninety', 30, None])

  + Exception Group Traceback (most recent call last):
  |   File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 49, in <module>
  |     validate_ages([24, -5, 'ninety', 30, None])
  |     ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |   File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 48, in validate_ages
  |     if errors: raise ExceptionGroup('Validation errors', errors)
  |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  | ExceptionGroup: Validation errors (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 45, in validate_ages
    |     validate_age(age)
    |     ~~~~~~~~~~~~^^^^^
    |   File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 40, in validate_age
    |     if age < 0: raise ValueError(f'Negative age: {age}')
    |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    | ValueError: Negative age: -5
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 45, in validate_ages
    |     validate_age(age)
    |     ~~~~~~~~~~~~^^^^^
    |   File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 39, in validate_age
    |     if not isinstance(age, int): raise TypeError(f'Not an integer {age}')
    |                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    | TypeError: Not an integer ninety
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 45, in validate_ages
    |     validate_age(age)
    |     ~~~~~~~~~~~~^^^^^
    |   File "d:\9billion_names_of_god\python\Python_books_HW\Романо_Крюгер\chapter_7.py", line 39, in validate_age
    |     if not isinstance(age, int): raise TypeError(f'Not an integer {age}')
    |                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    | TypeError: Not an integer None
    +------------------------------------
'''
# управление поток через exception
class ExitLoopException(Exception): pass
try:
    n = 100
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 42 * a + 17 * b + c == 5096:
                    raise ExitLoopException(a, b, c)
except ExitLoopException as ele:
    print(ele.args)
# context managers
from decimal import Context, Decimal, getcontext, setcontext, localcontext
one = Decimal('1')
three = Decimal('3')
orig_ctx = getcontext()
ctx = Context(prec=5)
setcontext(ctx)
print(f'{ctx}\n')
print('Custom decimal context:', one / three)
setcontext(orig_ctx)
print('Original context restored:', one / three)
with localcontext(Context(prec=5)) as ctx:
    print('Custom decimal context:', one / three)
print('Original context restored:', one / three)
# context manager class
class MyContextManager:
    def __init__(self):
        print('MyContextManager init', id(self))
    def __enter__(self):
        print('Entering with context')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{exc_type=} {exc_val=} {exc_tb=}')
        return True
ctx_mgr = MyContextManager()
print('About to enter with context')
with ctx_mgr as mgr:
    print('Inside with context')
    print(id(mgr))
    raise Exception('Exception inside with context')
    print('Never reached')
print('After with cotnext')