''' Алгоритмы поиска с возвратом '''

from typing import List, Optional
from dataclasses import dataclass

'''
    Дано двоичное дерево, необходимо найти и зафиксировать все узлы со значением 7 и вернуть список этих узлов.
'''
res = []
def pre_order(root: TreeNode):
    if root is None: return
    if root.val == 7: res.append(root)
    pre_order(root.left)
    pre_order(root.right)
'''
    Дано двоичное дерево, необходимо найти и зафиксировать все узлы со значением 7 и вернуть путь от корня к этим узлам.
'''
path = []
def pre_order(root: TreeNode):
    if root is None: return

    path.append(root)
    if root.val == 7:
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    path.pop()

'''
    В двоичном дереве необходимо найти все узлы со значением 7 и вернуть пути от корневого узла до этих узлов, при этом пути не должны содержать узлы со значением 3.
'''
def pre_order(root: TreeNode):
    if root is None or root.val == 3:
        return
    path.append(root)
    if root.val == 7:
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    path.pop()

''' Универсализцаия '''
@dataclass
class Choice:
    """Выбор — узел дерева (то, что можно добавить в путь)."""
    val: int = 0
    left: Optional["Choice"] = None
    right: Optional["Choice"] = None


class State:
    """Состояние — текущий путь обхода (список узлов)."""
    def __init__(self, path: Optional[List[Choice]] = None):
        self.path: List[Choice] = list(path) if path else []

    def append(self, choice: Choice) -> None:
        self.path.append(choice)

    def pop(self) -> Choice:
        return self.path.pop()

    def last(self) -> Optional[Choice]:
        return self.path[-1] if self.path else None

    def copy(self) -> "State":
        return State(self.path)

    def __bool__(self) -> bool:
        return bool(self.path)

    def __len__(self) -> int:
        return len(self.path)

    def __iter__(self):
        return iter(self.path)

    def __repr__(self) -> str:
        return f"State({[c.val for c in self.path]})"

def backtrack(state: State, choices: list[Choice], res: list[State]):
    if is_solution(state):
        record_solution(state, res)
        return
    for choice in choices:
        if is_valid(state, choice):
            make_choice(state, choice)
            backtrack(state, choice, res)
            undo_choice(state, choice)

def is_solution(state: list[TreeNode]) -> bool:
    return state and state[-1].val == 7

def record_solution(state: list[TreeNode], res: list[list[TreeNode]]):
    res.append(list(state))

def is_valid(state: list[TreeNode], choice: TreeNode) -> bool:
    return choice is not None and choice.val != 3

def make_choice(state: list[TreeNode], choice: TreeNode):
    state.append(choice)

def undo_choice(state: list[TreeNode], choice: TreeNode):
    state.pop() 

''' Задача о перестановках '''

'''
    Дан массив целых чисел, в котором отсутствуют повторяющиеся элементы. Необходимо вернуть все возможные перестановки.
'''
def backtrack(state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]):
    if len(state) == len(choices):
        res.append(list(state))
        return
    for i, choice in enumerate(choices):
        if not selected[i]:
            selected[i] = True
            state.append(choice)
            backtrack(state, choices, selected, res)
            selected[i] = False
            state.pop()

def permutations_i(nums: list[int]) -> list[list[int]]:
    res = []
    backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)

''' Есть равные элементы '''
def backtrack(state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]):
    if len(state) == len(choices):
        res.append(list(state))
        return
    duplicated = set[int]()
    for i, choice in enumerate(choices):
        if not selected[i] and choice not in duplicated:
            duplicated.add(choice)
            selected[i] = True
            state.append(choice)
            backtrack(state, choices, selected, res)
            selected[i] = False
            state.pop()

''' Задача о сумме подмножеств '''

'''
    Дан массив положительных целых чисел nums и целевое положительное целое число target. 
    Необходимо найти все возможные комбинации элементов, сумма которых равна target. 
    В массиве нет повторяющихся элементов, каждый элемент можно выбрать несколько раз. 
    Вернуть эти комбинации в виде списка, в котором не должно быть повторяющихся комбинаций.
'''
def backtrack(state: list[int], target: int, total: int, choices: list[int], res: list[list[int]]):
    if total == target:
        res.append(list(state))
        return
    for i in range(len(choices)):
        if total + choices[i] > target: continue
        state.append(choices[i])
        backtrack(state, target, total + choices[i], choices, res)
        state.pop()

def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
    state = []
    total = 0
    res = []
    backtrack(state, target, total, nums, res)
    return res

'''
    С обрезкой повторений
'''
def backtrack(state: list[int], target: int, start: int, choices: list[int], res: list[list[int]]):
    if target == 0:
        res.append(list(state))
        return
    for i in range(start, len(choices)):
        if target - choices[i] < 0:
            break
        state.append(choices[i])
        backtrack(state, target - choices[i], choices, i, res)
        state.pop()

def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
    state = []
    nums.sort()
    start = 0
    res = []
    backtrack(state, target, start, nums, res)
    return res

''' Задача об n ферзях '''
'''
    Согласно правилам шахмат, ферзь может атаковать фигуры, находящиеся на одной строке, одном столбце или одной диагонали. 
    Дано n ферзей и шахматная доска размером n×n. Требуется найти расстановку, при которой ферзи не могут атаковать друг друга.
'''
def backtrack(row: int, n: int, state: list[list[str]], res: list[list[list[str]]], cols: list[bool], diags1: list[bool], diags2: list[bool]):
    if row == n:
        res.append([list(row) for row in state])
        return
    for col in range(n):
        diag1 = row - col + n - 1
        diag2 = row + col
        if not cols[col] and not diags1[diag1] and not diags2[diag2]:
            state[row][col] = 'Q'
            cols[col] = diags1[diag1] = diags2[diag2] = True
            backtrack(row + 1, n, state, res, cols, diags1, diags2)
            state[row][col] = '#'
            cols[col] = diags1[diag1] = diags2[diag2] = False

def n_queens(n: int) -> list[list[list[str]]]:
    state = [['#' for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)
    diags2 = [False] * (2 * n - 1)
    res = []
    backtrack(0, n, state, res, cols, diags1, diags2)
    return res