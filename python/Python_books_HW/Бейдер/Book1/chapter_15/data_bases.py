import sqlite3
import os
db_path = os.path.join('python', 'Python_books_HW', 'Бейдер', 'chapter_15', 'test_database.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()
query = "SELECT datetime('now', 'localtime');"
results = cursor.execute(query)
row = results.fetchone()
print(row)
connection.close()
with sqlite3.connect(db_path) as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    results = cursor.execute(query)
    row = results.fetchone()
    time = row[0]
print(time)
create_table = """
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);"""
insert_values = """
INSERT INTO People VALUES(
    'Ron',
    'Obvious',
    42
);"""
with sqlite3.connect(db_path) as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS People")
    cursor.execute(create_table)
    cursor.execute(insert_values)
values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28),
)
with sqlite3.connect(db_path) as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS People")
    cursor.execute("""
        CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT           
        );""")
    cursor.executemany("INSERT INTO People VALUES(?, ?, ?);", values)
    cursor.execute("SELECT * FROM People")
    for row in cursor.fetchall():
        print(row)