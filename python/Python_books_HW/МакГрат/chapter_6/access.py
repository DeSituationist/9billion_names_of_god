file = open('example.txt', 'w')
print('File name:', file.name)
print('File open mode:', file.mode)
print('Readable:', file.readable())
print('Writable:', file.writable())
def get_status(f): return 'Closed' if (f.closed != False) else 'Open'
print('File status:', get_status(file))
file.close()
print('File status:', get_status(file))