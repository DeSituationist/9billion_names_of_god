def display(s):
    '''Printing argument'''
    print(s)
display(display.__doc__)
display(r'C:\Program Files')
display('\nHellow' + 'Python')
display('Python in easy steps\n'[7:])
display('p' in 'Python')
display('P' in 'Python')
snack = '{} and {}'.format('Burger', 'Fries')
print('\nReplaced:', snack)
snack = '{1} and {0}'.format('Burger', 'Fries')
print('Replaced:', snack)
snack = '%s and %s'%('Milk', 'Cookies')
print('\nSubstituted:', snack)
string = 'python in easy steps'
print('\nCaptitalized:\t', string.capitalize())
print('\nTitled:\t\t', string.title())
print('\nCentered\t', string.center(30, '*'))
print('\nUppercase:\t', string.upper())
print('\nJoined:\t\t', string.join('**'))
print('\nJustified:\t', string.rjust(30, '*'))
print('\nReplaced:\t', string.replace('s', '*'))
s = 'Röd'
print('\nRed string:', s)
print('Type:', type(s), '\tLength:', len(s))
s = s.encode('utf-8')
print('\nEncoded string:', s)
print('Type:', type(s), '\tLength:', len(s))
s = s.decode()
print(f'\nDecoded string {s}')
print(f'Type {type(s)}\t length: {len(s)}')
import unicodedata
for i in range(len(s)): print(s[i], unicodedata.name(s[i]), sep = ' : ')
s = b'Gr\xc3\xb6n'
print('Green string:', s.decode('utf-8'))
s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print('Green string:', s)