'''
class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)
    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)
    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)
    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)
    def __len__(self) : return len(self.data)
    def __getitem__(self, key) : return self.data[key]
    def __and__(self, other) : return self.intersect(other)
    def __or__(self, other) : return self.union(other)
    def __repr__(self) : return 'Set: ' + repr(self.data)
    def __iter__(self) : return iter(self.data)
if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    print(x.union(Set([1, 4, 7])))
    print(x | Set([1, 4, 6]))
'''
class Set(list):
    def __init__(self, value = []):
        list.__init__(self)
        self.concat(value)
    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)
    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res
    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)
    def __and__(self, other) : return self.intersect(other)
    def __or__(self, other) : return self.union(other)
    def __repr__(self) : return 'Set: ' + list.__repr__(self)
if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    y = Set([2, 1, 3, 4, 5, 6])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)