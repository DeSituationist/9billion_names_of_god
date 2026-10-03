''' Массив '''
arr : list[int] = [0] * 5

def insert(nums: list[int], num: int, index: int):
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num

def remove(nums: list[int], num: int, index: int):
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]

def traverse(nums: list[int]):
    count = 0
    for i in range(len(nums)):
        count += nums[i]
    for num in nums:
        count += num
    for i, num in enumerate(nums):
        count += nums[i]
        count += num

def linear_search(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def extend(nums: list[int], enlrage: int) -> list[int]:
    res = [0] * (len(nums) + enlrage)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

''' Связный список '''
class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None

n0, n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
n0.next, n1.next, n2.next = n1, n2, n3

def insert(n0: ListNode, P: ListNode):
    n1 = n0.next
    P.next = n1
    n0.next = P

def remove(n0: ListNode):
    if not n0.next: return
    P = n0.next
    n1 = P.next
    n0.next = n1

def access(head: ListNode, index: int) -> ListNode | None:
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

def find(head: ListNode, target: int) -> int:
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None
        self.prev: ListNode | None = None

''' Список '''
nums: list[int] = []
num: int = nums[1]

nums.append(3)
nums.insert(3, 6)
nums.pop(3)

count = 0
for i in range(len(nums)): count += nums[i]

for num in nums: count += num

nums1 = [1, 3, 7, 8]
nums += nums1

nums.sort()

class MyList:
    def __init__(self):
        self._capacity: int = 10
        self._arr: list[int] = [0] * self._capacity
        self._size: int = 0
        self._extend_ratio: int = 2

    def size(self) -> int: return self._size

    def capacity(self) -> int: return self._capacity

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size: raise IndexError(' Индекс выходит за границы. ')
        return self._arr[index]

    def set(self, num: int, index: int):
        if index < 0 or index >= self._size: raise IndexError(' Индекс выходит за границы. ')
        self._arr[index] = num

    def add(self, num: int):
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        if index < 0 or index >= self._size: raise IndexError(' Индекс выходит за границы. ')
        if self._size == self.capacity():
            self.extend_capacity()
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self[j]
        self._arr[index] = num
        self._size += 1

    def remove(self, index: int) -> int:
        if index < 0 or index >= self._size: raise IndexError(' Индекс выходит за границы. ')
        num = self._arr[index]
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        self._size -= 1
        return num

    def extend_capacity(self):
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
        self._capacity = len(self._arr)

    def to_array(self) -> list[int]:
        return self._arr[: self._size]
