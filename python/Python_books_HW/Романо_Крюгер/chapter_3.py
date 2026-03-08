# if/elif/else
late = True
if late:
    print('I need to call my manager')
else:
    print('no need to call my manager')
income = 150000
if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 100000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45
print(f'You will pay: ${income * tax_coefficient} in taxes')
alert_system = 'email'
error_severity = 'critical'
error_message = 'something gone wrong'
def send_email(mail, msg):
    print(f'Sent mail to {mail} with message {msg}') 
if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        send_email('admin@example.com', error_message)
    elif error_severity == 'medium':
        send_email('support1@example.com', error_message)
    else:
        send_email('support2@example.com', error_message)
# Тернарный оператор
order_total = 247
if order_total > 100:
    discount = 25
else:
    discount = 0
print(order_total, discount)
discount = 25 if order_total > 100 else 0
print(order_total, discount)
# match/case/case _
day_number = 412
match day_number:
    case 1 | 2 | 3 | 4 | 5:
        print('Weekday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:  # Шаблон подстановщик - wildcard
        print(f'{day_number} is not a valid day number')
# for
for number in [0, 1, 2, 3, 4]: print(number)
for number in range(5): print(number)
print(list(range(10)))
print(list(range(3, 8)))
print(list(range(-10, 10, 4)))
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)): print(position, surnames[position])
for position, surname in enumerate(surnames): print(position, surname)
# iterable
people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)
people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)
for age, person in zip(ages, people):
    print(person, age)
insturruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']
for age, person, insturument in zip(ages, people, insturruments):
    print(age, person, insturument)
for data in zip(ages, people, insturruments):
    print(*data)
# while
n = 39
remainders = []
while n > 0:
    remainder = n % 2
    remainders.append(remainder)
    n //= 2
remainders.reverse()
print(remainders)
n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
remainders.reverse()
print(remainders)
people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23, 24, 23, 21]
position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1
# break/continue
from datetime import date, timedelta
today = date.today()
tomorrow = today + timedelta(days=1)
products = [
    {'sku': '1', 'expiration_date': today, "price": 100.0},
    {'sku': '2', 'expiration_date': tomorrow, "price": 50},
    {'sku': '3', 'expiration_date': today, "price": 20},
]
for product in products:
    print('Proccessing sku', product['sku'])
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8
    print('Sku', product['sku'], 'price now is', product['price'])
items = [0, None, 0.0, True, 0, 7]
found = False
for item in items:
    print('scanning', item)
    if item:
        found = True
        break
if found:
    print('At least one item is True')
else:
    print('All items evaluate to False')
class DriverException(Exception): pass
people = [("James", 18), ("Kirk", 9), ("Lars", 13), ("Robert", 8)]
driver = None
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
else:  # nobreak 
    raise DriverException('Driver not found')
# := моржовый оператор
'''
value, modulus = 5, 7
remainder = value % modulus
if remainder: print(f'Not divisable {remainder=}')
if remainder := value % modulus: print(f'Not divisable {remainder=}')
flavors = ['pistaschio', 'malga', 'vanilla', 'chocolate']
prompt = 'Choose your flavor:'
print(flavors)
while True:
    choice = input(prompt)
    if choice in flavors: break
    print(f'Sorry, no {choice} flavor')
print(f'You chose {choice}')
prompt = 'Choose your flavor:'
print(flavors)
while (choice := input(prompt)) not in flavors:
    print(f'Sorry, no {choice} flavor')
print(f'You chose {choice}')
'''
# Генератор простых чисел
primes = []
upto = 100
for n in range(2, upto + 1):
    is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime: primes.append(n)
print(primes)
primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)
customers = [
    dict(id=1, total=200, coupon_code="F20"), # F20: фиксированная скидка, £20
    dict(id=2, total=150, coupon_code="P30"), # P30: процентная скидка, 30 %
    dict(id=3, total=100, coupon_code="P50"), # P50: процентная скидка, 50 %
    dict(id=4, total=110, coupon_code="F15"), # F15: фиксированная скидка, £15
]
for customer in customers:
    match customer['coupon_code']:
        case 'F20': customer['discount'] = 20.0
        case 'F15': customer['discount'] = 15.0
        case 'P30': customer['discount'] = customer['total'] * 0.3
        case 'P50': customer['discount'] = customer['total'] * 0.5
        case _: customer['discount'] = 0.0
for customer in customers: print(customer['id'], customer['total'], customer['discount'])
customers = [
    dict(id=1, total=200, coupon_code="F20"), # F20: фиксированная скидка, £20
    dict(id=2, total=150, coupon_code="P30"), # P30: процентная скидка, 30 %
    dict(id=3, total=100, coupon_code="P50"), # P50: процентная скидка, 50 %
    dict(id=4, total=110, coupon_code="F15"), # F15: фиксированная скидка, £15
] 
discounts = {
    "F20": (0.0, 20.0), # каждое значение — (процент, фиксированная сумма)
    "P30": (0.3, 0.0),
    "P50": (0.5, 0.0),
    "F15": (0.0, 15.0),
}
for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discounts.get(code, (0.0, 0.0))
    customer['discount'] = percent * customer['total'] + fixed
for customer in customers: print(customer['id'], customer['total'], customer['discount'])
# itertools
from itertools import count
for n in count(5, 3):
    if n > 20:
        break
    print(n, end= ', ')
from itertools import compress
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))