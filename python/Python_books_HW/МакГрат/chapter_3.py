nums = [0, 1, 2, 3, 4, 5]
quarter = ['January', 'Feburary', 'March']
print('First month :', quarter[0])
print('Second month :', quarter[1])
print('Third month :', quarter[2])
coords = [[1, 2, 3], [4, 5, 6]]
print('\nTop left 0, 0:', coords[0][0])
print('Bottom right 1, 2:', coords[1][2])
print('\nSecond moth first letter:', quarter[1][0])
basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']
print('Basket list:', basket)
print('Basket elements:', len(basket))
basket.append('Damson')
print('Appended:', basket)
print('Last item removed:', basket.pop())
print('Basket list:', basket)
basket.extend(crate)
print('Extended:', basket)
del basket[1]
print('Item removed:', basket)
del basket[1:3]
print('Slice removed:', basket)
colors_tuple = ('Red', 'Green', 'Red','Blue', 'Red')
a, b, c, d, e = colors_tuple
phonetic_set = {'alpha', 'bravo', 'charlie'}
zoo = ('Kangoroo', 'Leopard', 'Moose')
print('Tuple:', zoo, '\tlength:', len(zoo))
print(type(zoo))
bag = {'Red', 'Green', 'Blue'}
bag.add('Yellow')
print('\nset:', bag, '\tlength:', len(bag))
print(type(bag))
print('\nIs green in bag set?', 'Green' in bag)
print('Is Orange in bag set?', 'Orange' in bag)
box = {'Red', 'Purple', 'Yellow'}
print('\nSet:', box, '\t\tlength', len(box))
print('Common for both sides:', bag.intersection(box))
dict = {'name': 'Bob', 'ref': 'Python', 'sys': 'Win'}
print('Dictionary:', dict)
print('\nReference:', dict['ref'])
print('\nKeys:', dict.keys())
del dict['name']
dict['user'] = 'Tom'
print('\nDictionary:', dict)
print('\nIs there a name key?:', 'name' in dict)
num = int(input('Please enter a number: '))
if num > 5:
    print('Number exceeds 5')
elif num < 5:
    print('Number is less than 5')
else:
    print('Number is 5')
if num > 7 and num < 9:
    print('Number is 8')
if num == 1 or num == 3:
    print('number is 1 or 3')
i = 4
while i < 4:
    print('\nOuter loop iteration:', i)
    i += 1
j = 1
while j < 4:
    print('\nInner loop iteration:', j)
    j += 1
chars = ['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
dict = {'name': 'Mike', 'ref': 'Python', 'sys': 'Win'}
print('\nelements:\t', end = ' ')
for item in chars:
    print(item, end=' ')
print('\nEnumerated:', end = ' ')
for item in enumerate(chars):
    print(item, end = ' ')
print('\nZipped:\t', end = ' ')
for item in zip(chars, fruit):
    print(item, end = ' ')
print('\nPaired: ')
for key, value in dict.items():
    print(key, '=', value)
for i in range(4):
    for j in range(4):
        if i == 1 and j == 1: continue
        print('Running i=', i, 'j=', j)
        if i == 2 and j == 1:
            print('Breaks inner loop at i = 2 j = 1')