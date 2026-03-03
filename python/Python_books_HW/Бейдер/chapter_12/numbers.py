import csv
path_to_nums = 'python/Python_books_HW/Бейдер/chapter_12/numbers.csv'
numbers = [
    [1, 2],
    [3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
with open(path_to_nums, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in numbers:
        writer.writerow(row)
with open(path_to_nums, 'r') as file:
    reader = csv.reader(file)
    info = [[int(x) for x in row ] for row in reader]
    print(info)