''' Деревья '''
class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

p = TreeNode(0)
n1.left = p
p.left = n2
n1.left = n2 # удаление p

''' BFS - broad first search - поиск в ширину '''
from collections import deque
def level_order(root: TreeNode | None) -> list[int]:
    queue: deque[TreeNode] = deque()
    queue.append(root)
    res = []
    while queue:
        node: TreeNode = queue.popleft()
        res.append(node.val)
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)
    return res

''' DFS - depth first search - поиск в глубину '''
res = []
def pre_order(root: TreeNode | None):
    ''' Прямой обход '''
    if root is None: return
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)

def in_order(root: TreeNode | None):
    ''' Симметричный обход '''
    if root is None: return
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

def post_order(root: TreeNode | None):
    ''' Обратный обход '''
    if root is None: return
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)

class ArrayBinaryTree:
    def __init__(self, arr: list[int | None]):
        self._tree = list(arr)

    def size(self): return len(self._tree)

    def val(self, i: int) -> int | None:
        if i < 0 or i >= self.size(): return None
        return self._tree[i]

    def left(self, i: int) -> int | None:
        return 2 * i + 1

    def right(self, i: int) -> int | None:
        return 2 * i + 2

    def parent(self, i: int) -> int | None:
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        self.res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def dfs(self, i: int, order: str):
        if self.val(i) is None: return
        if order == 'pre':
            self.res.append(self.val(i))
        
        self.dfs(self.left(i), order)
        
        if order == 'in':
            self.res.append(self.val(i))
        
        self.dfs(self.right(i), order)
        
        if order == 'post':
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order = 'pre')
        return self.res

    def in_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order='in')
        return self.res

    def post_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order='post')
        return self.res

''' Поиск в бинарном дереве поиска '''
def search(self, num: int) -> TreeNode | None:
    cur = self._root
    while cur is not None:
        if cur.val < num: cur = cur.right
        elif cur.val > num: cur = cur.left
        else: break
    return cur

def insert(self, num: int):
    if self._root is None:
        self._root == num
        self._root = TreeNode(num)
        return
    cur, pre = self._root, None
    while cur is not None:
        if cur.val == num: return
        pre = cur
        if cur.val < num:
            cur = cur.right
        else:
            cur = cur.left
    node = TreeNode(num)
    if pre.val < num:
        pre.right = node
    else:
        pre.left = node

def remove(self, num: int):
    if self._root is None: return
    cur, pre = self._root, None
    while cur is not None:
        if cur.val == num:
            break
        pre = cur
        if cur.val < num:
            cur = cur.right
        else:
            cur = cur.left
    if cur is None: return
    if cur.left is None or cur. right is None:
        child = cur.left or cur.right
        if cur != self._root:
            if pre.left == cur: pre.left = child
            else: pre.right = child
    else:
        tmp: TreeNode = cur.right
        while tmp.left is not None:
            tmp = tmp.left
        self.remove(tmp.val)
        cur.val = tmp.val

''' АВЛ - деревья '''
class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.height: int = 0
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def height(self, node: TreeNode | None) -> int:
        if node is not None: return node.height
        return -1

    def update_height(self, node: TreeNode | None):
        node.height = max([self.height(node.left), self.height(node.right)]) + 1

    def balance_factor(self, node: TreeNode | None): 
        if node is None: return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, node: TreeNode | None):
        child = node.left
        grand_child = child.right
        child.right = node
        node.left = grand_child
        self.update_height(node)
        self.update_height(child)
        return child

    def left_rotate(self, node: TreeNode | None):
        child = node.right
        grand_child = child.left
        child.left = node
        node.right = grand_child
        self.update_height(node)
        self.update_height(child)
        return child

    def rotate(self, node: TreeNode | None):
        balance_factor = self.balance_factor(node)
        if balance_factor > 1:
            if self.balance_factor(node.left) >= 0: return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        elif balance_factor < -1:
            if self.balance_factor(node.right) <= 0:
                return self.balance_factor(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        return node