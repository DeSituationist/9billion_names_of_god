import sys
import glob
import hashlib
'''
# First ver
def find_duplicates(filenames):
    matches = []
    for i in range(len(filenames)):
        left = filenames[i]
        for j in range(i):
            right = filenames[j]
            if same_bytes(left, right):
                matches.append((left, right))
    return matches

def same_bytes(left_name, right_name):
    left_bytes = open(left_name, 'rb').read()
    right_bytes = open(right_name, 'rb').read()
    return left_bytes == right_bytes

if __name__ == '__main__':
    patterns = sys.argv[1:]
    filenames = []
    for pat in patterns:
        filenames.extend(glob.glob(pat))
    print(filenames)
    duplicates = find_duplicates(filenames)
    for left, right in duplicates:
        print(left, right)

# Naive Hashed ver
# Хэширование — это математическое отображение (функция), которая преобразует произвольный набор данных (например, содержимое файла) 
# в уникальный числовой код (хэш-код).
# В книге вы используете простую функцию naive_hash, которая суммирует ASCII-коды байтов и делит их на 13. 
# Это демонстрирует принцип работы хэширования, хотя в реальных системах используются более сложные алгоритмы (например, SHA-256).
# Файл a1.txt содержит "aaa" (ASCII-коды: 97, 97, 97).
# sum(data) = 291, 291 % 13 = 6 → хэш-код 6.
# Файл a2.txt также содержит "aaa" → хэш-код 6.
# Файлы b1.txt и b2.txt содержат "bb" → хэш-код 10.
def naive_hash(data):
    return sum(data) % 13

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, 'rb').read()
        hash_code = naive_hash(data)
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups

# Теперь сложность алгоритма O(N^2/groups)
'''
# SHA-256 ver
# Если groups = N, то сложность становится O(N)
# То есть для каждого файла своя группа
'''
example = bytes('hash', 'utf-8')
for i in range(1, len(example) + 1):
    substring = example[: i]
    hash = hashlib.sha256(substring).hexdigest()
    print(f'{substring}\n{hash}')

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, 'rb').read()
        hash_code = hashlib.sha256(data).hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups

if __name__ == '__main__':
    txt_files = glob.glob(r"D:\9billion_names_of_god\python\Python_books_HW\Уилсон\chp3_test\*.txt")
    if not txt_files:
        print("No .txt files found in that folder.")
    else:
        groups = find_groups(txt_files)
        for filenames in groups.values():
            print(', '.join(sorted(filenames)))
'''
# HomeWork
# Using I/O API for large files
def find_groups(filenames):
    groups = {}
    for fn in filenames:
        hasher = hashlib.sha256()
        with open(fn, 'rb') as txt:
            chucked_data = txt.read(128)
            while chucked_data:
                hasher.update(chucked_data)
                chucked_data = txt.read(128)
            hash_code = hasher.hexdigest()
            if hash_code not in groups:
                groups[hash_code] = set()
            groups[hash_code].add(fn)
    return groups

if __name__ == '__main__':
    txt_files = glob.glob(r"D:\9billion_names_of_god\python\Python_books_HW\Уилсон\chp3_test\*.txt")
    if not txt_files:
        print("No .txt files found in that folder.")
    else:
        groups = find_groups(txt_files)
        for filenames in groups.values():
            print(', '.join(sorted(filenames)))

# Почему hash(l23) и h ash("l23") работают корректно, тогда как hash([l23]) вызывает исключение?
# Так как список это изменяемый тип данных, а функция hash принимает только неизменяемые типы данных
def hash_codes_to_ints(hash_code):
    return int(hash_code, base=16)
def sha_for_line(txt):
    lines_groups = {}
    with open(txt, 'rb') as txt:
        line = txt.readline()
        while line:
            hash_code = hashlib.sha256(line).hexdigest()
            if hash_code not in lines_groups:
                lines_groups[hash_code] = set()
            lines_groups[hash_code].add(line)
            line = txt.readline()  
    return [hash_codes_to_ints(x) for x in lines_groups]

# Версия без групп
def sha_for_line(txt):
    hashes = set()
    with open(txt, 'rb') as f:
        for line in f:
            hashes.add(hashlib.sha256(line).hexdigest())
    return [int(h, 16) for h in hashes]
# Насколько равномерно распределены хеш-коды? Как меняется распреде­ление при обработке файлов большего размера?
# Распределение хэш кодов остается равномерным в независимости от размера файла