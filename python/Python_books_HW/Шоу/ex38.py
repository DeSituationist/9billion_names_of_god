ten_things = 'Яблоки Апельсины Вороны Телефоны Свет Сахар'
print('Погодите, тут меньше 10 объектов. Давайте исправит это.')
stuff = ten_things.split(' ') #split(ten_things, ' ')
more_stuff = ['День', 'Ночь', 'Песня', 'Мишка', 'Кукурузка', 'Банан', 'Девочка', 'Мальчик']
while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff)
    print('Добавляем: ', next_one)
    stuff.append(next_one) #append(stuff, next_one)
    print(f'Теперь у нас {len(stuff)} объектов')
print('Итак: ', stuff)
print('Давайте-ка кое-что сделаем с нашими объектами.')
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) #join(stuff, ' ')
print('#'.join(stuff[3:5])) #join(stuff[3:5], '#')