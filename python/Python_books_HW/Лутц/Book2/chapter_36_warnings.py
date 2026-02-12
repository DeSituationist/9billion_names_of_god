#Выход из множества циклов.
class ExitLoop(Exception) : pass
try:
    while  True:
        while True:
            for i in range(10):
                if i > 3: raise ExitLoop
                print('loop3:', i)
            print('loop2')
        print('loop3')
except ExitLoop:
    print('continuing')
#Как предупреждение.
'''
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        break
'''