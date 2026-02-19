#Объявление функции с двумя переменными
def cheese_and_crakers(cheese_count, boxes_of_crackers):
    #Вывод f-строки
    print(f'У нас есть {cheese_count} сырков')
    #Вывод f-строки
    print(f'У нас есть {boxes_of_crackers} пачек чипсов')
    #Вывод строки
    print('Этого достаточно для вечеринки!')
    #Вывод строки
    print('Погнали!\n')
#Вывод строки
print('Мы можем непосредственно передать числа функции:')
#Вызов функции с передачей двух аргументов позиционно
cheese_and_crakers(20, 30)
#Вывод строки
print('Или, мы можем использовать переменные из нашего сценария:')
#Инициализация переменной
amount_of_cheese = 10
#Инициализация переменной
amount_of_crackers = 50
#Вызов функции с передачей двух аргументов позиционно
cheese_and_crakers(amount_of_cheese, amount_of_crackers)
#Вывод строки
print('Мы даже можем выполнять вычисления внутри функции:')
#Вызов функции с передачей двух аргументов позиционно
cheese_and_crakers(10+20, 5+6)
#Вывод строки
print('И объединять переменные с вычислениями:')
#Вызов функции с передачей двух аргументов позиционно
cheese_and_crakers(amount_of_cheese + 100, amount_of_crackers + 1000)
def my_func(*args):
    print('This are the arguments given:', *args)
my_func(1, 2, 3, 4, 5)
my_func('a' + 'b', 'c')
my_func(1 + 2, 'c', 50.0)
my_func(1 + 2, 'c', my_func(50.0, 1, 2, 3))
my_func(my_func, my_func, my_func)