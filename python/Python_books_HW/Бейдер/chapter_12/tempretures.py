import csv
path_to_temps = 'python/Python_books_HW/Бейдер/chapter_12/tempretures.csv'
daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
]
file = open(path_to_temps, 'w', newline='')
writer = csv.writer(file)
for temp_list in daily_temperatures:
    writer.writerow(temp_list)
file.close()
file = open(path_to_temps, 'r')
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()
path_to_emps = 'python/Python_books_HW/Бейдер/chapter_12/employees.csv'
file = open(path_to_emps, 'r')
reader = csv.DictReader(file)
print(reader.fieldnames)
for row in reader: print(row)
file.close()