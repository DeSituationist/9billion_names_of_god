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
#Chapter_2
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
#Chapter_3
from typing import *

drinks = ['hot chocolate', 'coffee', 'coffee without coffein']
flavors = ['caramel', 'vanilla', 'mint', 'raspberry', 'without toppings']
toppings = ['chocolate', 'cinnamon', 'caramel']

def menu(choices: List[str], title: str, prompt: str) -> str:
    print(title)
    print('-' * 30)
    for i, item in enumerate(choices, 1):
        print(i, item)
    choice = int(input(prompt)) - 1
    return choices[choice]

drink = menu(drinks, 'Main drinks:', 'Enter drink number: ')
flavor = menu(flavors, 'Flavors:', 'Enter flavor number: ')
topping = menu(toppings, 'Toppings: ', 'Enter topping number: ')
print('Your order: ')
print('Main drink: ', drink)
print('Flavor: ', flavor)
print('Topping: ', topping)
print('Thanks for order')
#Chapter_4
from typing import *

drinks = ['hot chocolate', 'coffee', 'coffee without coffein']
flavors = ['caramel', 'vanilla', 'mint', 'raspberry', 'without toppings']
toppings = ['chocolate', 'cinnamon', 'caramel']

def menu(choices: List[str], title: str, prompt: str) -> str:
    print(title)
    print('-' * 30)
    for i, item in enumerate(choices, 1):
        print(i, item)
    while True:
        try:
            choice = input(prompt)
            if not choice in 'xX':
                choice = int(choice) - 1
            else:
                return ''
            return choices[choice]
        except ValueError:
            print(f"Please enter a number (1 to {len(choices)}).")
        except IndexError:
            print(f"Please enter a number within 1 to {len(choices)}.")

drink = menu(drinks, 'Main drinks:', 'Enter drink number: ')
flavor = menu(flavors, 'Flavors:', 'Enter flavor number: ')
topping = menu(toppings, 'Toppings: ', 'Enter topping number: ')

print('Your order: ')
print('Main drink: ', drink)
print('Flavor: ', flavor)
print('Topping: ', topping)
print('Thanks for order')

#Chapter_5
from typing import *

drinks = ['hot chocolate', 'coffee', 'coffee without coffein']
flavors = ['caramel', 'vanilla', 'mint', 'raspberry', 'without toppings']
toppings = ['chocolate', 'cinnamon', 'caramel']

def menu(choices: List[str], title: str, prompt: str) -> str:
    print(title)
    print('-' * 30)
    for i, item in enumerate(choices, 1):
        print(i, item)
    while True:
        try:
            choice = input(prompt)
            if not choice in 'xX':
                choice = int(choice) - 1
            else:
                return ''
            return choices[choice]
        except ValueError:
            print(f"Please enter a number (1 to {len(choices)}).")
        except IndexError:
            print(f"Please enter a number within 1 to {len(choices)}.")

def read_menu(filename: str) -> List[str]:
    names = []
    with open(filename) as file:
        names = file.readlines()
        names = [name.strip() for name in names]
    return names

drink = menu(read_menu('drinks.txt'), 'Main drinks:', 'Enter drink number: ')
flavor = menu(read_menu('flavors.txt'), 'Flavors:', 'Enter flavor number: ')
topping = menu(read_menu('toppings.txt'), 'Toppings: ', 'Enter topping number: ')

print('Your order: ')
print('Main drink: ', drink)
print('Flavor: ', flavor)
print('Topping: ', topping)
print('Thanks for order')
'''