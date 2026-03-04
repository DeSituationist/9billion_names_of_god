path_to_ships = 'python/Python_books_HW/Бейдер/chapter_12/starships.txt'
with open(path_to_ships, 'w', newline='') as ships:
    ships.writelines(['Discovery\n', 'Enterprise\n', 'Defiant\n', 'Voyager'])

with open(path_to_ships, 'r') as ships:
    for line in ships: print(line, end='')

with open(path_to_ships, 'r') as ships:
    line = ships.readline()
    if line.startswith('D'): print('\n' + line)