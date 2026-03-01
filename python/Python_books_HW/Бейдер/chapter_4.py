paragraph = """This plaпet has-or rather had-a proЫem, which was
this: most of the people liviпg оп it were uпhappy for pretty much
of the time. Мапу solutioпs were suggested for this proЫem, but
most of these were largely сопсеrпеd with the movemeпts of small
greeп pieces of paper, which is odd because оп the whole it wasп't
the small greeп pieces of paper tt1at were uпhappy. """
paragraph_1 = """This plaпet has-or rather had-a proЫem, which was 
this: most of the people liviпg оп it were uпhappy for pretty much
of the time. Мапу solutioпs were suggested for this proЫem, but
most of these were largely сопсеrпеd with the movemeпts of small
greeп pieces of paper, which is odd because оп the whole it wasп't
the small greeп pieces of paper tt1at were uпhappy. """
paragraph_2 = "This plaпet has-or rather had-a proЫem, which was   \
this: most of the people liviпg оп it were uпhappy for pretty much \
of the time. Мапу solutioпs were suggested for this proЫem, but    \
most of these were largely сопсеrпеd with the movemeпts of small   \
greeп pieces of paper, which is odd because оп the whole it wasп't \
the small greeп pieces of paper tt1at were uпhappy. "
paragraph_3 = 'This plaпet has-or rather had-a proЫem, which was   \
this: most of the people liviпg оп it were uпhappy for pretty much \
of the time. Мапу solutioпs were suggested for this proЫem, but    \
most of these were largely сопсеrпеd with the movemeпts of small   \
greeп pieces of paper, which is odd because оп the whole it wasп\'t\
the small greeп pieces of paper tt1at were uпhappy.'
print(paragraph)
print(paragraph_1)
print(paragraph_2)
print(paragraph_3)
print(len(paragraph))
str1, str2 = 'abc', 'def'
print(str1 + str2)
print(str1 + ' ' + str2)
print('bazinga'[2:])
def str_to_lower(*args, mthd = 'lower()'):
        for i in args: print(eval(f'"{i}".{mthd}'))
str_to_lower('Animals', 'Badger', 'Honey Bee', 'Honey Badger')
str_to_lower('Animals', 'Badger', 'Honey Bee', 'Honey Badger', mthd = 'upper()')
for i in ['     Filet Mignan', 'Brisket     ', '   Cheesburger  ']:
        print(i.strip())
for i in ["Becomes", "becomes", "BEAR", " bEautiful"]:
        print(i.startswith('be'))
print(input('Say something: '))
print(input('Say something: ').lower())
print('The length of ur answer is', len(input('Say something: ')))
print('The first letter of ur password is', input('Tell me your passwrod: ')[0])
s_num = '123'
print(int(s_num) * 123)
s_num = '123'
print(float(s_num) * 123.4)
a, b = int(input('Enter first number: ')), int(input('Enter second number: '))
print(f'Result of {a} + {b} = {a + b}')
weight, animal = 0.2, 'newt'
print(f'{weight} kg is the wegiht of {animal}')
print('{weight} kg is the wegiht of {animal}'.format(weight = weight, animal = animal))
print('AAA'.find('a'))
print("Somebody said something to Samantha.".replace('s', 'x'))
txt = input('Enter some text')
encode_map = {'a': '4', 'b': '8', 'e': '3', 'l': '1', 'o': '0', 's': '5', 't': '7'}
print(''.join(encode_map[x] if x in encode_map.keys() else x for x in txt))