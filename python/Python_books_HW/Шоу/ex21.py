def add(a, b):
    print(f'Сложение {a} + {b}')
    return a + b
def substract(a, b):
    print(f'Вычитание {a} - {b}')
    return a - b
def multiply(a, b):
    print(f'Умножение {a} * {b}')
    return a * b
def divide(a, b):
    print(f'Деление {a} / {b}')
    return a / b
print('Давайте выполним несколько вычислений с помошью функций!')
age = add(30, 5)
height = substract(190, 4)
weight = multiply(35, 2)
iq = divide(250, 2)
print(f'Возраст: {age}, Рост: {height}, Вес: {weight}, IQ: {iq}')
print('Это головоломка.')
what = add(age, (substract(height, multiply(weight, divide(iq, 2)))))
print('Получается: ', what, 'Вы можете вычислить вручную?')
what_easier = height - iq / 2 * weight + age
print(what_easier)