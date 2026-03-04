#import greeter
#print(greeter.greet('Ilia'))
from mypackages import math_mod as m_md, string_mod as s_md
area = m_md.area(5, 8)
print(s_md.shout(f'The area of a 5-by-8 rectangle is {area}'))