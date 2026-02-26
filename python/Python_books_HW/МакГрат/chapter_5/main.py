import sys, keyword
print('Python version:', sys.version)
print('Python interpreter location:', sys.executable)
print('Python keywords:')
for word in keyword.kwlist: print(word)