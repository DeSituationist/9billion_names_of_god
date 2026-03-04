def cube(number: int) -> int:
    '''Returns number to the power of 3'''
    return number ** 3
def greet(name: str) -> None:
    '''Function that greets'''
    print(f'Hello {name}!')
def convert_cel_to_far(temp: float) -> float:
    '''Converts tempreture from celsius to farenheit'''
    return temp * (9 / 5) + 32
def convert_far_to_cel(temp: float) -> float:
    '''Converts tempreture from farenheit to celsius'''
    return (temp - 32) * (5 / 9)
celsius, farenheit = float(input('Enter tempreture in celsius: ')), float(input('Enter tempreture in farenheit: '))
print(f'{convert_cel_to_far(celsius):.2f}')
print(f'{convert_far_to_cel(farenheit):.2f}')
for num in range(2, 11): print(num)
num = 2
while num < 11:
    print(num)
    num += 1
def double_thrice(num: int) -> None:
    '''Doubles number three times'''
    for i in range(1, 4):
        print(num * (2 ** i))
double_thrice(2)
def invest(amount: int, rate: int, years: int) -> None:
    for i in range(1, years+1):
        amount += amount * rate
        print(f'year {i}: ${amount:.2f}')
invest(100, .05, 4)