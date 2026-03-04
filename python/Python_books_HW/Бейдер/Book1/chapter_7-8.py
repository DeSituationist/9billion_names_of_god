print(1 <= 1)
print(1 != 1)
print(1 != 2)
print('good' != 'bad')
print('good' != 'Good')
print(123 == '123')
print(3 < 4)
print(10 > 5)
print('jack' != 'jill')
print(42 != '42')
print((1 <= 1) and (1 != 1))
print(not(1 != 2))
print(('good' != 'bad') or False)
print(('good' != 'Good') and not(1 == 1))
print(False == (not True))
print((True and False) == (True and False))
print(not(True and ('A' == 'B')))
word = input('Give me a word: ')
if len(word) < 5: print('Length of word less then 5')
elif len(word) > 5: print('Length of word more then 5')
else: print('Equals to 5')
guess = int(input('Ive guessed a number: '))
if guess == 3: print('Youve won')
else: print('Youve lost')
num = int(input('Enter a positive integer: '))
for i in range(1, num):
    if num % i == 0: print(f'{i} is a factor of {num}')
while True:
    char = input('Please enter q or Q: ')
    if char.lower() != 'q':
        print('Bad boy')
    else:
        print('Good boy')
        break
flag = False
while flag != True:
    try:
        num = int(input('Enter an integer: '))
        print('Youve entered', num)
        flag = True
    except ValueError:
        print('Try again')
import random
def coin_flip() -> str:
    '''Returns heads or tails'''
    if random.randint(0, 1) == 0:
        return 'heads'
    else:
        return 'tails'
heads_total = 0
tails_total = 0
for trial in range(100):
    if coin_flip() == 'heads': heads_total += 1
    else: tails_total += 1
ratio = heads_total / tails_total
print(f'The ratio of heads to tails is {ratio:.2f}')    
def throw_a_dice() -> None:
    '''Throws a dice 10_000 times'''
    dropped = [0] * 7
    for i in range(10_000):
        got = random.randint(1, 6)
        dropped[got] += 1
    average = sum(i * dropped[i] for i in range(1, 7)) / 10_000
    print(average)
throw_a_dice()
def voting() -> None:
    '''Simulates voting'''
    times_won_all_three = 0
    chance_1 = 0.87
    chance_2 = 0.65
    chance_3 = 0.17
    for i in range(10_000):
        if random.randint(0, 1) >= chance_1 and random.randint(0, 1) >= chance_2 and random.randint(0, 1) >= chance_3:
            times_won_all_three +=1
    print(f'Percent of times president won: {times_won_all_three/10_000:.2%}')
voting()