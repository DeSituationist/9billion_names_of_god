''' Сложность O(1) - константная '''
def constant(n: int) -> int:
    count = 0
    size = 1_000_000_000
    for _ in range(size):
        count += 1
    return count

''' Сложность O(n) - линейная '''
def linear(n: int) -> int:
    count = 0
    for _ in range(n):
        count += 1
    return count

''' Сложность O(n^2) - квадратичная '''
def quadratic(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def bubble_sort(nums: list[int]) -> int:
    count = 0
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                tmp: int = nums[j]
                nums[j]= nums[j + 1]
                nums[j + 1] = tmp
            count += 3
    return count

''' Сложность O(2^n) - экспоненциальная '''
def exponental(n: int) -> int:
    count = 0
    base = 1
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    return count

def exp_recur(n: int) -> int:
    if n == 1:
        return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1

''' Сложность O(log n) - логарифмическая '''
def logarithmic(n: int) -> int:
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

def log_recur(n: int) -> int:
    if n <= 1:
        return 0
    return log_recur( n / 2 ) + 1

''' Сложность O(n*log n) - линейно-логарифмическая '''
def linear_log_recur(n: int) -> int:
    if n <= 1: return 1
    count = linear_log_recur( n // 2) + linear_log_recur( n // 2 )
    for _ in range(n):
        count += 1
    return count

''' Сложность O(n!) - факториальная '''
def factorial_recur(n: int) -> int:
    if n == 0: return 1
    count = 0
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count

''' Пространственная сложность '''
class Node:
    def __init__(self, x: int):
        self.val = x
        self.next: Node | None = None

def function() -> int:
    return 0

def algorithm(n) -> int: # Входные данные
    A = 0 # временные данные - константа
    b = 0 # временные данные - переменная
    node = Node(0) # временныве данные - объект
    c = function() # пространство стэка
    return A + b + c # выходные данные

def algorithm(n: int):
    a = 0 # O(1)
    b = [0] * 10000 # O(1)
    if n > 10: nums = [0] * n # O(n) 

def function() -> int:
    return 0

def loop(n: int):       # Временная сложность O(n) Пространственная O(1) - стэк освобождается после каждого выозова
    for _ in range(n):
        function()

def recur(n: int):      # Временная сложность O(n) Пространтсвенная O(n) - стэк хранит все вызовы до возврата из рекурсии
    if n == 1: return
    return recur(n - 1)

''' Сложность O(1) - константная '''
def function() -> int:
    return 0

def constant(n: int):
    a = 0
    nums = [0] * 10000
    node = Node(0)
    for _ in range(n):
        c = 0
    for _ in range(n): 
        function()

''' Сложность O(n) - линейная '''
def linear(n : int):
    nums = [0] * n # Занимает O(n)
    hmap = dict[int, str]() # Занимает O(n)
    for i in range(n): hmap[i] = str[i]

def linear_recur(n: int):
    print('Рекурсия = ', n)
    if n == 1: return
    linear_recur(n - 1)

''' Сложность O(n ^ 2) - квадратичная '''
def quadratic(n : int):
    num_matrix = [[0] * n for _ in range(n)] # Двумерный список O(n ^ 2)

def quadratic_recur(n: int):
    if n <= 0: return 0
    nums = [0] * n # Средняя длина n / 2
    return quadratic_recur(n - 1) # n

''' Сложность O(2 ^ n) - экспоненциальная '''
def build_tree(n : int):
    if n == 0: return None
    root = Node(0)
    root.left = build_tree(n - 1) # На каждом шаге алгоритма делимся на 2
    root.right = build_tree(n - 1) # и так делаем n раз => O(2 ^ n)
    return root
