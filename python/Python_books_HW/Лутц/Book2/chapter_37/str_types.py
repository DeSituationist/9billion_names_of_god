b = b'spam'
s = 'eggs'
print(type(b), type(s))
print(b[0], s[0])
s = s.encode()
print(s)
b = b.decode()
print(b)
b = b'A\xc3\x84B\xc3\xa8C' #Текст, закодированный в utf-8
s = b.decode('utf-8')
print(s)
t = s.encode('cp500') #кодируем в IBM-EBCDIC
print(t)
u = t.decode('cp500')
print(u)
b = bytes('abc', 'ascii')
print(b)
s = 'spam'
c = bytearray(s, 'latin-1')
print(c)
print(c[0])
c[0] = ord('x')
print(c[0])
print(c)
c[1] = b'Y'[0]
print(c)