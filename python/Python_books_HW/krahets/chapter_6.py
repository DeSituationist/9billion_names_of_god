''' Хэш таблица '''
hmap: dict = {}

hmap[123] = 'Ivan'
hmap[175] = 'John'
hmap[157] = 'Max'

name: str = hmap[157]
hmap.pop(123)

for key, value in hmap.items(): 
    print(key, '->', value)

for key in hmap.keys():
    print(key)

for value in hmap.values():
    print(value)

class Pair:
    def __init__(self, key: int, val: str):
        self.key = val
        self.val = val

class ArrayHashMap:
    def __init__(self):
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int):
        index = key % 100
        return index

    def get(self, key: int) -> str:
        index: int = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val

    def put(self, key: int, val: str):
        pair = Pair(key, val)
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int):
        index: int = self.hash_func(key)
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        result: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def key_set(self) -> list[int]:
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)

    def value_set(self) -> list[str]:
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)

    def print(self):
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, '->', pair.val)

class HashMapChaining:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets = [[] for _ in range(self.capacity)]

    def hash_func(self, key: int) -> int:
        return key % self.capacity

    def load_factor(self) -> float:
        return self.size / self.capacity

    def get(self, key: int) -> str | None:
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                return pair.val
        return None

    def put(self, key: int, val: str):
        if self.load_factor() > self.load_thres: self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return
        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def extend(self):
        buckets = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + ' -> ' + pair.val)
        print(res)

class HashMapOpenAddressing:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets: list[Pair | None] = [None] * self.capacity
        self.TOMBSTONE = Pair(-1, '-1')

    def hash_func(self, key: int) -> int:
        return key % self.capacity

    def load_factor(self) -> float:
        return self.size / self.capacity

    def find_bucket(self, key: int) -> int:
        index = self.hash_func(key)
        first_tombstone = -1
        while self.buckets[index] is not None:
            if self.buckets[index].key == key:
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tombstone
                return index
            if first_tombstone == -1 and self.buckets[index] is self.TOMBSTONE:
                first_tombstone = index
            index = (index + 1) % self.capacity
        return index if first_tombstone == - 1 else first_tombstone

    def get(self, key: int) -> str:
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            return self.buckets[index].val
        return None

    def put(self, key: int, val: str):
        if self.load_factor > self.load_thres: self.extend()
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index].val = val
            return
        self.buckets[index] = Pair(key, val)
        self.size += 1

    def remove(self, key: int):
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1

    def extend(self):
        buckets_tmp = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0
        for pair in buckets_tmp:
            if pair not in [None, self.TOMBSTONE]:
                self.put(pair.key, pair.val)

    def print(self):
        for pair in self.buckets:
            if pair is None:
                print('None')
            elif pair is self.TOMBSTONE:
                print('TOMBSTONE')
            else:
                print(pair.key, '->', pair.val)

''' Функции хэширования '''
def add_hash(key: str) -> int:
    hash = 0
    modulus = 1000000007
    for c in key: hash += ord(c)
    return hash % modulus

def mul_hash(key: str) -> int:
    hash = 0
    modulus = 1000000007
    for c in key: hash = 31 * hash * ord(c)
    return hash % modulus

def xor_hash(key: str) -> int:
    hash = 0
    modulus = 1000000007
    for c in key: hash ^= ord(c)
    return hash % modulus

def rot_hash(key: str) -> int:
    hash = 0
    modulus = 1000000007
    for c in key: hash = (hash << 4) ^ (hash >> 28) ^ ord(c)
    return hash % modulus  