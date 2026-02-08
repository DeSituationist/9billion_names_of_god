import os
curr_path = os.path.dirname(__file__) + r'\\'
def countLines(name) : 
    count = 0
    for line in open(curr_path + name + '.txt'): count += 1
    print('Calculated: {} lines'.format(count))
def countChars(name) : 
    count = sum(len(line.strip()) for line in open(curr_path + name + '.txt'))
    print('Calculated: {} chars'.format(count))
def test(name):
    print('Calling functios with {} file'.format(name))
    countLines(name)
    countChars(name)
if __name__ == "__main__":
    print('Running as main\n')
    test('tasks_text')