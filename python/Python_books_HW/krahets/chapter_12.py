''' Разделяй и влавствуй '''

''' binary search recur '''
def dfs(nums: list[int], target: int, i: int, j: int) -> int:
    if i > j: return -1
    m = (i + j) // 2
    if nums[m] < target:
        return dfs(nums, target, m + 1, j)
    elif nums[m] > target:
        return dfs(nums, target, i, m - 1)
    else: 
        return m

def binary_search(nums: list[int], target: int) -> int:
    n = len(nums)
    return dfs(nums, target, 0, n - 1)

''' Построение двоичного дерева на основе inorder и preorder '''
class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

def dfs(
    preorder: list[int],
    inorder_map: dict[int, int],
    i: int,
    l: int,
    r: int,
) -> TreeNode | None:
    if r - l < 0:
        return None
    root = TreeNode(preorder[i])
    m = inorder_map[preorder[i]]
    root.left = dfs(preorder, inorder_map, i + 1, l, m - 1)
    root.right = dfs(preorder, inorder_map, i + 1 + m - l, m + 1, r)
    return root

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    inorder_map = {val: i for i, val in enumerate(inorder_map)}
    root = dfs(preorder, inorder_map, 0, 0, len(inorder) - 1)
    return root

''' Задача о Ханойских башнях 
Даны три стержня, обозначенные как A, B и C. В начальном состоянии на стержне A находятся n дисков, расположенных в порядке увеличения размера сверху вниз. 
Необходимо переместить эти n дисков на стержень C, сохраняя их первоначальный порядок, как показано на рис. 12.10. 
При перемещении дисков необходимо соблюдать следующие правила:

диск можно снять только с вершины одного стержня и положить на вершину другого стержня;
за один раз можно перемещать только один диск;
меньший диск всегда должен находиться выше большего диска.
'''
def move(src: list[int], tar: list[int]):
    # Перемещение диска с src на tar
    pan = src.pop()
    tar.append(pan)

def dfs(i: int, src: list[int], buf: list[int], tar: list[int]):
    ''' Решение задачи Ханойской башни(i) src-исходный buf-промежуточный tar-цель '''
    if i == 1: 
        move(src, tar)
        return
    # Первая подзадача f(i - 1): переместить i-1 дисков с src на buf через tar
    dfs(i - 1, src, tar, buf)
    # Вторая подзадача f(1): переместить оставшийся диск с src на tar
    move(src, tar)
    # Третья подзадача f(i-1): переместить все диски с buf на tar через src
    dfs(i - 1, buf, src, tar)

def solve_hanota(A: list[int], B: list[int], C: list[int]):
    n = len(A)
    dfs(n, A, B, C)