def some_func(N, K):
    numbers = []
    for i in range(0, N, K):
        print(f'В начале значение i равно {i}')
        numbers.append(i)
        print('Текущие значения: ', numbers)
        print(f'В конце значение i равно {i}')
    print('Значения')
    for num in numbers:
        print(num)
some_func(3, 1)
some_func(10, 3)