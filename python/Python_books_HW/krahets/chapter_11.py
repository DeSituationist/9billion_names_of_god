''' Сортировка '''

''' Selection sort - Сортировка выбором '''
def selection_sort(nums: list[int]):
    n = len(nums)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]

''' Bubble sort - Сортировка пузырьком '''
def bubble_sort(nums: list[int]):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

def bubble_sort_with_flag(nums: list[int]):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        flag = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag: break

''' Insertion sort - Сортировка вставками '''
def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = base

''' Quick sort - Быстрая сортировка '''
def partition(nums: list[int], left: int, right: int) -> int:
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1 # Находим меньше опорного nums[left]
        while i < j and nums[j] <= nums[left]:
            i += 1 # Находим элемент больше
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[left] = nums[left], nums[i] # Перемещение опрного элемента
    return i # индекс опрного элемента  

# Теперь рекурсивно это для всех подмассивов как только длина подмассива становится 1 прекращаем рекурсию

def quick_sort(nums: list[int], left: int, right: int):
    if left >= right: return
    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)

def median_three( nums: list[int], left: int, mid: int, right: int) -> int:
    """ Выбор медианы из трех кандидатов """
    l, m, r = nums[left], nums[mid], nums[right]
    if (l <= m <= r) or (r <= m <= l):
        return mid # m находится между l и r
    if (m <= l <= r) or (r <= l <= m):
        return left # l находится между m и r
    return right

def partition(nums: list[int], left: int, right: int) -> int:
    """ Разделение по методу стражей (медиана из трех) """
    # Использование nums[left] в качестве опорного элемента
    med = median_three(nums, left, (left + right) // 2, right)
    # Перемещение медианы в начало массива
    nums[left], nums[med] = nums[med], nums[left]
    # Использование nums[left] в качестве опорного элемента
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1 # Поиск элемента, меньшего опорного, справа налево
        while i < j and nums[i] <= nums[left]:
            i += 1 # Поиск элемента, большего опорного, слева направо
    # Обмен элементов
    nums[i], nums[j] = nums[j], nums[i]
    # Перемещение опорного элемента на границу подмассивов
    nums[i], nums[left] = nums[left], nums[i]
    return i # Возврат индекса опорного элемента

''' Сортировка слиянием '''
def merge(nums: list[int], left: int, mid: int, right: int):
    tmp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1
    for k in range(0, len(tmp)):
        nums[left + k] = tmp[k]

def merge_sort(nums: list[int], left: int, right: int):
    if left >= right: return
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    merge(nums, left, mid, right)

''' Heap sort - Пирамидальная сортировка '''
def sift_down(nums: list[int], n: int, i: int):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        ma = i
        if l < n and nums[l] > nums[ma]:
            ma = l
        if r < n and nums[r] > nums[ma]:
            ma = r
        if ma == i: break
        nums[i], nums[ma] = nums[ma], nums[i]
        i = ma

def heap_sort(nums: list[int]):
    for i in range(len(nums) // 2 - 1, -1, -1):
        sift_down(nums, len(nums), i)
    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, i, 0)

''' Блочная сортировка - bucket sort '''
def bucket_sort(nums: list[float]):
    k = len(nums) // 2
    buckets = [[] for _ in range(k)]
    for num in nums:
        i = int(num * k)
        buckets[i].append(num)
    for bucket in buckets:
        bucket.sort()
    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1

'''Сортировка посчетом - counting sort '''
def counting_sort_naive(nums: list[int]):
    m = 0
    for num in nums:
        m = max(m, num)
    counter = [0] * (m + 1)
    for num in nums:
        counter[num] += 1
    counter = [0] * (m + 1)
    for num in nums:
        counter[num] += 1
    i = 0
    for num in range(m + 1):
        for _ in range(counter[num]):
            nums[i] = num
            i += 1