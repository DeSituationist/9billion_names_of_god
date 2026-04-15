'''
#Chapter_1
print('Welcome to coffee shop')
name = input('Enter your name: ')
drink = input('Enter your drink: ')
flavor = input('Enter your flavor: ')
topping = input('Enter your topping: ')
print('Your order, ', name)
print('Main drink: ', drink)
print('Flavor: ', flavor)
print('Topping: ', topping)
print('Thanks for order')
chapter_2
drinks = ['hot chocolate', 'coffee', 'coffee without coffein']
flavors = ['caramel', 'vanilla', 'mint', 'raspberry', 'without toppings']
toppings = ['chocolate', 'cinnamon', 'caramel']
print('List of drinks available: ')
for i, item in enumerate(drinks, 1):
    print(i, item)
drink = int(input('Enter drink number: ')) - 1
print('List of favors available: ')
for i, item in enumerate(flavors, 1):
    print(i, item)
flavor = int(input('Enter flavor number: ')) - 1
print('List of toppings available: ')
for i, item in enumerate(toppings, 1):
    print(i, item)
topping = int(input('Enter topping number: ')) - 1
print('Your order: ')
print('Main drink: ', drinks[drink])
print('Flavor: ', flavors[flavor])
print('Topping: ', toppings[topping])
print('Thanks for order')
'''