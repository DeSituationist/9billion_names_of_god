print('-'*30 + 'TASK-1' + '-'*30)
def oops(): raise IndexError
def check():
    try:
        oops()
    except:
        print('running')
check()
print('check done')
print('-'*30 + 'TASK-2' + '-'*30)
class MyError(Exception) : pass
def oops(): raise MyError()
def check():
    try:
        oops()
    except (IndexError, MyError) as exc:
        print('caught: ', exc.__class__)
check()
print('check done')
print('-'*30 + 'TASK-3' + '-'*30)
import sys
import traceback as tb
def safe(func, *args, **kargs):
    try:
        func(*args, **kargs)
    except:
        print('Caught: ', sys.exc_info()[0], sys.exc_info()[1])
        tb.print_exc()
safe(check(), None, None)