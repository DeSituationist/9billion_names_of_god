#Имортируем функцию argv из модуля sys 
#from sys import argv
#Передаем значения переменным из argv
#script, filename = argv
#Открываем файл по имени с кодировкой utf-8
filename = input('Please enter file that u wish to open: ')
txt = open(filename, encoding='utf-8')
#Выводим f-строку
print(f'содержимое файла {filename}: ')
#Выводим содержимое файла
print(txt.read())
#Выводим строку
print('Снова введите имя файла:')
#Получаем значение input и передаем переменной
file_again = input('> ')
#Открываем файл по имени с кодировкой utf-8
txt_again = open(file_again, encoding='utf-8')
#Выводим содержимое файла
print(txt_again.read()) 
txt.close()
txt_again.close()