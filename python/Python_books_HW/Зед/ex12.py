import pydoc
print('hello', input())
age = input('Сколько тебе лет? ')
height = input('Каков твой рост? ')
weight = input('Сколько ты весишь? ')
print(f'Итак, тебе {age} лет, в тебе {height} см роста и {weight} кг веса.')
pydoc.help(input)