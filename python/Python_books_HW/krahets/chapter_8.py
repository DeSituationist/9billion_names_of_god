''' Куча/Приоритетная очередь '''
import heapq
min_heap, flag = [], 1 # минимальная
max_heap, flag = [], -1 # максимальная
heapq.heappush(max_heap, flag * 1)
heapq.heappush(max_heap, flag * 3)
heapq.heappush(max_heap, flag * 2)
heapq.heappush(max_heap, flag * 5)
heapq.heappush(max_heap, flag * 4)

peek: int = flag * max_heap[0] # 5
val = flag * heapq.heappop(max_heap) # 5
val = flag * heapq.heappop(max_heap) # 4
val = flag * heapq.heappop(max_heap) # 3
val = flag * heapq.heappop(max_heap) # 2
val = flag * heapq.heappop(max_heap) # 1

size: int = len(max_heap)

is_empty: bool = not max_heap

min_heap: list[int] = [1, 3, 2, 5, 4]
heapq.heapify(min_heap)

class MaxHeap:
    def __init__(self, nums: list[int]):
        self.max_heap = nums
        for i in range(self.parent(self.size() - 1), -1, -1): self.sift_down(i)
    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def peek(self) -> int: return self.max_heap[0]

    def push(self, val: int):
        self.max_heap.append(val)
        self.sift_up(self.size() - 1)

    def sift_up(self, i: int):
        while True:
            p = self.parent(i)
            if p < 0 or self.max_heap[i] <= self.max_heap[p]:
                break
            self.swap(i, p)
            i = p

    def pop(self) -> int:
        if self.is_empty(): raise IndexError('Куча пуста')
        self.swap(0, self.size() - 1)
        val = self.max_heap.pop()
        self.sift_down(0)
        return val

    def sift_down(self, i: int):
        while True:
            l, r, ma = self.left(i), self.right(i), i
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]: ma = l
            if r < self.size() and self.max_heap[r] > self.max_heap[ma]: ma = r
            if ma == i: break
            self.swap(i, ma)
            i = ma
''' 
    Найти k наибольших элементов
    в неупорядоченном массиве длины n
'''

def top_k_heap(nums: list[int], k: int) -> list[int]:
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap