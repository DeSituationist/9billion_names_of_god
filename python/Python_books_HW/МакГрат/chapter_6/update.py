text = 'The political slogan "Workers of the world unite!" is from communist manifesto'
with open('update.txt', 'w') as file:
    file.write(text)
    print('\nFile closed?', file.closed)
print('And now?', file.closed)
with open('update.txt', 'r+') as file:
    text = file.read()
    print('\nString:', text)
    print('\nPosition in file now', file.tell())
    position = file.seek(33)
    print('Position in file now:', file.tell())
    file.write('All lands')
    file.seek(59)
    file.write('the tombstone of karl marx.')
    file.seek(0)
    text = file.read()
    print('\nString:', text)