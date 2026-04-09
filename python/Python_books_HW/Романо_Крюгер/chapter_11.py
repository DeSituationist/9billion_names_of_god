# custom debug
def debug(*msg, print_separator=True):
    print(*msg)
    if print_separator:
        print('-' * 40)
debug('Data is corrupted...')
debug('Different', 'Strings', 'Arent a problem')
debug('After while loop', print_separator=False)
# with time
from time import sleep
def debug(*msg, timestamp=[None]):
    from time import time
    print(*msg)
    if timestamp[0] is None:
        timestamp[0] = time()
    else:
        now = time()
        print(f'Time elapsed: {now - timestamp[0]:.3f}s')
        timestamp[0] = now
debug('Start')
sleep(0.3)
debug('First step')
sleep(0.5)
debug('Second step')
# logging
import logging
logging.basicConfig(
    filename = 'ch11.log',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt = '%m%d%Y %I:%M:%S %p',
)
mylist = [1, 2, 3]
logging.info('Starting to process "mylist"...')
for position in range(4):
    try:
        logging.debug(
            'Value at position %s is %s',
            position,
            mylist[position],
        )
    except IndexError:
        logging.exception('Faulty position: %s', position)
logging.info('Done processing my list')
# profiling
# python -m cProfile 
def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
def calc_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5
def is_int(n):
    return n.is_integer()
triples = calc_triples(1000)