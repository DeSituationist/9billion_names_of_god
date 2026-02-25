things = ['а', 'б', 'в', 'г']
print(things[1])
things[1] = 'я'
print(things[1])
print(things)
stuff = {'name':'Ilya', 'age':21, 'weight': ...}
print(stuff['name'])
print(stuff['age'])
print(stuff['weight'])
stuff['city'] = 'Saint-Petersburg'
print(stuff['city'])
stuff[1] = 'Horray'
stuff[2] = 'No'
print(stuff[1])
print(stuff[2])
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)
states = {
    'Russia':'RU',
    'Germany':'DE',
    'Uzbekistan':'UZ',
    'Zimbabwe':'ZW',
    'Turkey':'TR'
}
cities = {
    'UZ':'Gazly',
    'TR':'Anatolia',
    'DE':'Munchen'
}
cities['ZW'] = 'Gveru'
cities['RU'] = 'Moscow'
print('-' * 10)
print('In country ZW there is a city: ', cities['ZW'])
print('In country RU there is a city: ', cities['RU'])
print('-' * 10)
print('Abbreviature Turkey: ', states['Turkey'])
print('Abbreviature Germany: ', states['Germany'])
print('-' * 10)
print('In Turkey there is a city: ', cities[states['Turkey']])
print('In Germany there is a city: ', cities[states['Germany']])
print('-' * 10)
for state, abbrev in states.items():
    print(f'{state} has abbreviature {abbrev}')
print('-' * 10)
for abbrev, city in cities.items():
    print(f'In country {abbrev} there is a city {city}')
print('-' * 10)
for state, abbrev in states.items():
    print(f'In country {state} people use abbreviature {abbrev}')
    print(f'and there is a city {cities[abbrev]}')
print('-' * 10)
state = states.get('USA')
if not state:
    print('Sorry, USA doesn\'t exsist or has been destroyed')
city = cities.get('US', 'Doesn\'t exsist')
print(f'In country \'US\' there is a city: {city}')
