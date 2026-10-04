''' Стэк '''
stack: list[int] = []

stack.append(1)
stack.append(2)
stack.append(3)

peek: int = stack[-1]
pop: int = stack.pop()
size: int = len(stack)
is_empty: bool = len(stack) == 0

class ListNode():
    def __init__(self, val: int):
        self.val = val
        self.next: ListNode | None = None

class LinkedListStack:
    def __init__(self):
        self._peek = ListNode | None
        self._size: int  = 0

    def size(self) -> int: return self._size

    def is_empty(self) -> bool: return self._size == 0

    def push(self, val: int):
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('Стек пуст')
        return self._peek.val

    def to_list(self) -> list[int]:
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr

class ArrayStack:
    def __init__(self):
        self._stack: list[int] = []

    def size(self) -> int:
        return len(self._stack)

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, item: int):
        self._stack.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('Стэк пуст')
        return self._stack.pop()

    def peek(self) -> int:
        if self.is_empty(): raise IndexError('Стек пуст')
        return self._stack[-1]

    def to_list(self) -> list[int]:
        return self._stack

''' Очередь '''
from collections import deque
que: deque[int] = deque()
que.append(1)
que.append(2)
que.append(3)

front: int = que[0]
pop: int = que.popleft()
size: int = len(que)
is_empty: bool = len(que) == 0

class LinkedListQueue:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size: int = 0

    def size(self) -> int: return self._size

    def is_empty(self) -> bool: return self._size == 0

    def push(self, num: int):
        node = ListNode(num)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def pop(self) -> int:
        num = self.peek()
        self._front = self._front.next
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty(): raise IndexError(' Очередь пуста ')
        return self._front.val

    def to_list(self) -> list[int]:
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue

class ArrayQueue:
    def __init__(self, size: int):
        self._nums: list[int] = [0] * size
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int: return len(self._nums)

    def size(self) -> int: return self._size

    def is_empty(self) -> bool: return self._size == 0

    def push(self, num: int):
        if self._size == self.capacity(): raise IndexError(' Очередь полна ')
        rear: int = (self._front + self._size) % self.capacity()
        self._nums[rear] = num
        self._size += 1

    def pop(self) -> int:
        num: int = self.peek()
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty(): raise IndexError('Очередь пуста')
        return self._nums[self._front]

    def to_list(self) -> list[int]:
        res = [0] * self.size()
        j: int = self._front
        for i in range(self.size()):
            res[i] = self._nums[(j % self.capacity())]
            j += 1
        return res

''' Двустороняя очередь '''
from collections import deque

deq: deque[int] = deque()

deq.append(2)
deq.append(3)
deq.append(4)

front: int = deq[0]
rear: int = deq[-1]

pop_front: int = deq.popleft()
pop_rear: int = deq.pop()

size: int = len(deq)

is_empty: bool = len(deq) == 0

class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None
        self.prev: ListNode | None = None

class LinkedListDeque:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size: int = 0

    def seize(self): return self._size

    def is_empty(self): return self._size == 0

    def push(self, num: int, is_front: bool):
        node = ListNode(num)
        if self.is_empty(): self._front = self._rear = node
        elif is_front:
            self._front.prev = node
            node.next = self._front
            self._front = node
        else:
            self._rear.next = node
            node.prev = self._rear
            self._rear = node
        self._size += 1

    def push_first(self, num: int):
        self.push(num, True)

    def push_last(self, num: int):
        self.push(num, False)

    def pop(self, is_front: bool):
        if self.is_empty(): raise IndexError(' Двустороняя очередь пуста ')
        if is_front:
            val: int = self._front.val
            fnext: ListNode | None = self._front.next
            if fnext != None:
                fnext.prev = None
            self._front.next = None
            self._front = fnext
        else:
            val: int = self._rear.val
            rprev: ListNode | None = self._rear.prev
            if rprev != None:
                rprev.next = None
            self._rear.prev = None
            self._rear = rprev
        self._size -= 1
        return val

    def pop_first(self) -> int:
        return self.pop(True)

    def pop_last(self) -> int:
        return self.pop(False)

    def peek_first(self) -> int:
        if self.is_empty(): raise IndexError(' Двустороняя очередь пуста ')
        return self._front.val

    def peek_last(self) -> int:
        if self.is_empty(): raise IndexError(' Двустороняя очередь пуста')
        return self._rear.val

    def to_array(self) -> list[int]:
        node = self._front
        res = [0] * self.size()
        for i in range(self.size()):
            res[i] = node.val
            node = node.next
        return res

class ArrayDeque:
    def __init__(self, capacity: int):
        self._nums: list[int] = [0] * capacity
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int:
        return len(self._nums)

    def size(self) -> int:
        return self._size

    def is_empty(self):
        return self._size == 0

    def index(self, i: int) -> int:
        return (i + self.capacity()) % self.capacity()

    def push_first(self, num: int):
        if self._size == self.capacity():
            print(' Двустороняя очередь полна. ')
            return
        self._front = self.index(self._front - 1)
        self._nums[self._front] = num
        self._size += 1

    def push_last(self, num: int):
        if self._size == self.capacity():
            print(' Двустороняя очередь полна. ')
            return 
        rear = self.index(self._front + self._size)
        self._nums[rear] = num
        self._size += 1

    def pop_first(self) -> int:
        num = self.peek_first()
        self._front = self.index(self._front + 1)
        self.size -= 1
        return num

    def pop_last(self) -> int:
        num = self.peek_last()
        self._size -= 1
        return num

    def peek_first(self) -> int:
        if self.is_empty(): raise IndexError(' Двустороняя очередь пуста. ')
        return self._nums[self._front]

    def peek_last(self) -> int:
        if self.is_empty(): raise IndexError(' Двустороняя очередь пуста. ')
        last = self.index(self._front + self._size - 1)
        return self._nums[last]

    def to_array(self) -> list[int]:
        res = []
        for i in range(self._size): res.append(self._nums[self.index(self.front + i)])
    