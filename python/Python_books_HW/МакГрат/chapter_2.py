a = 8
b = 2
print('Addition:\t', a, '+', b, '=', a + b)
print('Subtraction:\t', a, '-', b, '=', a - b)
print('Multiplication:\t', a, 'x', b, '=', a * b)
print('Division:\t', a, '/', b, '=', a / b)
print('Floor Division:\t', a, '//', b, '=', a // b)
print('Modulus:\t', a, '%', b, '=', a % b)
print('Exponent:\t', a, '**', b, '=', a ** b)
a = 8
b = 4
print('Assign Values:\t\t', 'a=', a, '\tb=', b)
a += b
print('Add & Assign:\t\t', 'a=', a, '(8 += 4)')
a -= b
print('Subtract & Assign:\t', 'a=', a, '(12-4)')
a *= b
print('Multiply * Assign:\t', 'a=', a, '(8 x 4)')
a /= b
print('Divide & Assign:\t', 'a=', a, '(32 / 4)')
a %= b
print('Modulus & Assign:\t', 'a=', a, '(8 % 4)')
nil = 0
num = 0
max = 1
cap = 'A'
low = 'a'
print('Equality:\t', nil, '==', num, nil == num)
print('Equality:\t', cap, '==', low, cap == low)
print('Inequality:\t', nil, '!=', max, nil != max)
print('Greater:\t', nil, '>', max, nil > max)
print('Lesser:\t', nil, '<', max, nil < max)
print('More or equal:\t', nil, '>=', num, nil >= num)
print('Less or equal:\t', max, '<=', num, max <= num)
a = True
b = False
print('And logic:')
print('a and a =', a and a)
print('a and b =', a and b)
print('b and b =', b and b)
print('\nOr logic:')
print('a or a =', a or a)
print('a or b =', a or b)
print('b or b =', b or b)
print('\nNot logic:')
print('not a =', not a)
print('not b =', not b)
a = 1
b = 2
print('\nVariable a is:', 'One' if (a == 1) else 'Not One')
print('Variable a is:', 'Even' if (a % 2 == 0) else 'Odd')
print('\nVariable b is:', 'One' if (b == 1) else 'Not One')
print('Variable b is:', 'Even' if (b % 2 == 0) else 'Odd')
max = a if (a > b) else b
print('\nGreate value is:', max)
a = 2
b = 4
c = 8
print('\nDefault order:\t', a, '*', c, '+', b, '=', a * c + b)
print('Forced order:\t', a, '* (', c, '+', b, ') =', a * (c + b))
print('\nDefault order:\t', c, '//', b, '-', a, '=', c // b - a)
print('Forced order:\t', c, '// (', b, '-', a, ') =', c // (b - a))

print('\nDefault order:\t', c, '%', a, '+', b, '=', c % a + b)
print('Forced order:\t', c, '% (', a, '+', b, ') =', c % (a + b))
print('\nDefault order:\t', c, '**', a, '+', b, '=', c ** a + b)
print('Forced order:\t', c, '** (', a, '+', b, ') =', c ** (a + b))
a = input('Enter a number: ')
b = input('Now enter another number: ')
sum = a + b
print('\nData type sum:', sum, type(sum))
sum = int(a) + int(b)
print('Data type sum:', sum, type(sum))
sum = float(sum)
print('Data type sum:', sum, type(sum))
sum = chr(int(sum))
print('Data type sum:', sum, type(sum))
a = 10
b = 5
print('a=', a, '\tb=', b)
a = a ^ b
b = a ^ b
a = a ^ b
print('a=', a, '\tb=', b)