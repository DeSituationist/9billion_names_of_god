import re
s = 'Bugger all down here on earth!'
b = b'Bugger all down here on earth!'
print(re.match('(.*) down (.*) on (.*)', s).groups())
print(re.match(b'(.*) down (.*) on (.*)', b).groups())