import csv
path_to_nums = 'python/Python_books_HW/Бейдер/chapter_12/fav_colors.csv'
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]
with open(path_to_nums, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name','favorite_color'])
    writer.writeheader()
    writer.writerows(favorite_colors)
path_to_emps = 'python/Python_books_HW/Бейдер/chapter_12/fav_colors.csv'
with open(path_to_emps, 'r') as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader: print(row)