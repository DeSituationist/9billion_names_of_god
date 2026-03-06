# Словарь со значением по умолчанию
name_for_userid = {
    352: 'Ellis',
    127: 'Bob',
    753: 'Gilbert',
}
def greeting(userid):
    print(f'Hello {name_for_userid[userid]}')
greeting(352)
#greeting(231)  # KeyError: 231
def greeting(userid):
    if userid in name_for_userid:
        print(f'Hello {name_for_userid[userid]}')
    else:
        print('Hello everyone')
greeting(231)
def greeting(userid):
    try:
        print(f'Hello {name_for_userid[userid]}')
    except KeyError:
        print('Hello everyone')
greeting(231)
def greeting(userid):
    print(f'Hello, {name_for_userid.get(userid, 'everyone')}')
greeting(352)
greeting(231)
# Сортировка словарей
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items()))
print(sorted(xs.items(), key=lambda x: x[1]))
import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
print(sorted(xs.items(), key=lambda x: x[1], reverse=True))
# Конструкции выбора на основе словарей
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()
print(dispatch_dict('mul', 2, 8))
# Странный словарь
insaine_dict = {True: 'Yes', 1: 'No', 1.0: 'Maybe'}  # Python считает все ключи одинаковыми и имеют одинаковое хэш значение, поэтому ключи не обновляются
# Так как при создании словаря ключи передаются по порядку слева направо, то Python переписывает одинаковый ключ новым значением
print(insaine_dict)
# Объединение словарей
xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}
zs = {}
zs.update(xs)
zs.update(ys)
print(zs)
ds = {**xs, **ys}
print(ds)
# Структурная печать словаря
import json
mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(json.dumps(mapping, indent=4, sort_keys=True))