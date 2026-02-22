#Импортируем функцию argv из модуля sys
from sys import argv
#Передаем значения из списка argv в переменные
script, input_file = argv
#Определяем функцию
def print_all(f):
    #Выводим все содержимое файла
    print(f.read())
#Определяем функцию
def rewind(f):
    #Возвращаемся в начало файла
    f.seek(0)
#Определяем функцию
def print_a_line(line_count, f):
    #Выводим строку из файла
    print(line_count, f.readline())
#Открываем файл
current_file = open(input_file)
#Выводим строку
print('Первым делом выведем этот файл целиком:\n')
print_all(current_file)
#Выводим строку
print('Теперь отмотаем назад, слово это кассета.')
rewind(current_file)
#Выводим строку
print('Выведем три строки:')
#Инициализируем переменную
current_line = 1
#Вызываем функцию с аргументами
print_a_line(current_line, current_file)
#Инкрементируем переменную
current_line += 1
#Вызываем функцию с аргументами
print_a_line(current_line, current_file)
#Инкрементируем переменную
current_line += 1
#Вызываем функцию с аргументами
print_a_line(current_line, current_file)