''' Двоичный поиск'''
def binary_search(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target: i = m + 1
        elif nums[m] > target: j = m - 1
        else: return m
    return -1

def binary_search_lcro(nums: list[int], target: int) -> int:
    ''' Левозамкнутый и правооткрытый интервал '''
    i, j = 0, len(nums)
    while i < j:
        m = (i + j) // 2
        if nums[m] < target: i = m + 1
        elif nums[m] > target: j = m
        else: return m
    return -1

'''
    Вставка с помощью бинарного поиска
    Дан упорядоченный массив nums длины n и элемент target. 
    В массиве отсутствуют повторяющиеся элементы. Необходимо вставить target в массив nums, сохраняя его упорядоченность. 
    Если элемент target уже существует в массиве, то вставить его слева от существующего. Вернуть индекс target после вставки.
'''
def binary_search_insertion_simple(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target: i = m + 1
        elif nums[m] > target: j = m - 1
        return m
    return i

def binary_search_insertion(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target: i = m + 1
        elif nums[m] > target: j = m - 1
        else: j = m -1 
    return i

def binary_search_left_edge(nums: list[int], target: int) -> int:
    i = binary_search_insertion(nums, target)
    if i == len(nums) or nums[i] != target: return -1
    return i

def binary_search_right_edge(nums: list[int], target: int) -> int:
    i = binary_search_insertion(nums, target + 1)
    j = i - 1
    if j == -1 or nums[j] != target: return -1
    return j

'''
    Дан массив целых чисел nums и целевой элемент target. 
    Необходимо найти в массиве два элемента, сумма которых равна target, и вернуть их индексы.
'''
def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target: return [i, j]
    return []

def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            return [dic[target - nums[i]], i]
        dic[nums[i]] = i