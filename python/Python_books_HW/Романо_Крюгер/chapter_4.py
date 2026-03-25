x = 3
def func(y):
    print(y)
func(x)
x = [1, 2, 3]
def func(x):
    x[1] = 42
func(x)
print(x)
# positional_arguments
def func(a, b, c):
    print(a, b, c)
func(1, 2, 3)
# named_arguments
def func(a, b, c):
    print(a, b, c)
func(a=1, c=3, b=2)
# positional_and_named
def func(a, b, c):
    print(a, b, c)
func(42, b=1, c=2)
# unboxing iterator
def func(a, b, c):
    print(a, b, c)
value = (1, 3, -7)
func(*value)
# unboxing dictionary
def func(a, b, c):
    print(a, b, c)
values = {'b': 1, 'c': 2, 'a': 42}
func(**values)
# combined
def func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)
func(1, *(2, 3), f=6, *(4, 5))
func(c=3, *(1, 2), **{'d': 4}, e=5, **{'f':6})
# non-mandatory parametrs
def func(a, b=4, c=88):
    print(a, b, c)
func(1)
# args
def minimum(*args):
    print(min(args))
minimum(1, 3, -7, 9)
# kwargs
def func(**kwargs):
    print(kwargs)
func(a=1, b=46, c=99)
def connect(**options):
    conn_params = {
        "host": options.get("host", "127.0.0.1"),
        "port": options.get("port", 5432),
        "user": options.get("user", ""),
        "pwd": options.get("pwd", ""),
    }
    print(conn_params)
# затем мы подключаемся к базе данных (закомментировано)
# db.connect(**conn_params)
connect()
connect(host="127.0.0.42", port=5433)
connect(port=5431, user="fab", pwd="gandalf")
# forced positinal
def func(a, b, /, c):  # a, b - только позиционно
    print(a, b, c)
func(1, 2, c=3)
# forced named
def func(a, b, *, c):  # c - только по имени
    print(a, b, c)
func(1, b=2, c=3)
def func_name(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters): ...
# изменяемы параметры по умолчанию кэшируются и сохраняют изменения
def func(a=[], b={}):
    print(a)
    print(b)
    print("#" * 12)
    a.append(len(a)) # это изменит значение по умолчанию для a
    b[len(a)] = len(a)
func()
func()
func()
# lambda funcs
adder_lambda = lambda a, b: a + b
to_upper_lambda = lambda a: a.upper()
