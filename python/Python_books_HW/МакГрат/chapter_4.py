global_var = 1
def my_vars():
    print('Global variable:', global_var)
    local_var = 2
    print('Local variable:', local_var)
    global inner_var
    inner_var = 3
my_vars()
print('Coerced global:', inner_var)
def echo(user):
    print('User:', user)
echo('Mike')
def echo(user, lang, sys):
    print('User:', user, 'language:', lang, 'Platform:', sys)
echo('Mike', 'Python', 'Windows')
echo(lang = 'Python', user = 'Mike', sys = 'Windows')
def echo(user, lang, sys = 'Linux'):
    print(f'User: {user} language: {lang} platform: {sys}')
echo(lang = 'Python', user = 'Ann')
def mirror(user = 'Carloe', lang = 'Python'):
    print('\nUser:', user, 'Language:', lang)
mirror()
mirror(lang = 'Python')
mirror(user = 'Tony')
mirror('Susan', 'cpp')
def sum(a, b) : return a + b
total = sum(8, 4)
print('Eight plus four is', total)
print('Eight plus four is', sum(8, 4))
num = input('Enter an int: ')
def square(num):
    if not num.isdigit(): return 'Invalid Entry'
    num = int(num)
    return num * num
print(num, 'squared is', square(num))
def function_1(x) : return x ** 2
def function_2(x) : return x ** 3
def function_3(x) : return x ** 4
callbacks = [function_1, function_2, function_3]
print('\nNamed functions:')
for function in callbacks : print('Result:', function(3))
callbacks = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
print('Anonymous functions:')
for function in callbacks: print('Result:', function(3))
def incrementer():
    i = 1
    while True:
        yield i
        i += 1
inc = incrementer()
print(next(inc))
print(next(inc))
print(next(inc))
def fibonacci_generator():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci_generator()
for i in fib:
    if i > 100:
        break
    else:
        print('Generated:', i)
day = 32
try:
    if day > 31:
        raise ValueError('Invalid Day Number')
except ValueError as msg:
    print('The program found an', msg)
finally:
    print('But today is a beautiful day anyway')
chars = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
def display(elem):
    assert type(elem) is int, 'Argument must be int'
    print(f'list element {elem} = {chars[elem]}')
elem = 4
display(elem)
elem = elem / 2
display(elem)