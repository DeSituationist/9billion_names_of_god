''' Динамическое программирование '''

'''
    Дана лестница с n ступенями, на каждом шаге можно подниматься на одну или две ступени. Сколько существует способов добраться до вершины лестницы?
'''
def backtrack(choices: list[int], state: int, n: int, res: list[int]) -> int:
    if state == n:
        res[0] += 1
    for choice in choices:
        if state + choice > n:
            continue
        backtrack(choices, state + choice, n, res)

def climbing_stairs_backtrack(n: int) -> int:
    choices = [1, 2]
    state = 0
    res = [0]
    backtrack(choices, state, n, res)

def dfs(i: int) -> int:
    if i == 1 or i == 2: return i
    count = dfs(i - 1) + dfs(i - 2)
    return count

def climbing_stairs_dfs(n: int) -> int:
    return dfs(n)

''' Используем сохранение повторяемых вызовов '''
def dfs(i: int, mem: list[int]) -> int:
    if i == 1 or i == 2:
        return i
    if mem[i]  != -1: return mem[i]
    count = dfs(i - 1, mem) + dfs(i - 2, mem)
    return count

def climbing_stairs_dfs_mem(n: int) -> int:
    mem = [-1] * (n + 1)
    return dfs(n, mem)

''' Через динамическое программирование снизу вверх '''
def climbing_stairs_dp(n: int) -> int:
    if n == 1 or n == 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[i]

def climbing_stairs_dp(n: int) -> int:
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

'''
    Дана лестница, по которой можно подниматься на одну или две ступени за раз. 
    На каждой ступени указана неотрицательная целочисленная стоимость, которую необходимо заплатить за подъём по этой ступени. 
    Дан неотрицательный целочисленный массив cost, где cost[i] обозначает стоимость i-й ступени, а cost[0] — стоимость на полу (начальная точка). 
    Необходимо вычислить минимальную стоимость достижения вершины.
'''
def min_cost_climbing_stairs_db(cost: list[int]) -> int:
    n = len(cost) - 1
    if n == 1 or n == 2: return cost[n]
    dp = [0] * (n + 1)
    dp[1], dp[2] = cost[1], cost[2]
    for i in range(3, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    return dp[n]

def min_cost_climbing_stairs_db(cost: list[int]) -> int:
    n = len(cost) - 1
    if n == 1 or n == 2: return cost[n]
    a, b = cost[1], cost[2]
    for i in range(3, n + 1):
        a, b = b, min(a, b) + cost[i]
    return b

'''
    Дана лестница с n ступенями, по которой можно подниматься на одну или две ступени за раз, но нельзя дважды подряд подняться на одну ступень. 
    Сколько существует способов подняться на вершину?
'''
def climbing_stairs_constraint_dp(n: int) -> int:
    if n == 1 or n == 2: return 1
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][1], dp[1][2] = 1, 0
    dp[2][1], dp[2][2] = 0, 1
    for i in range(3, n + 1):
        dp[i][1] = dp[i - 1][2]
        dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
    return dp[n][1] + dp[n][2]

'''
    Дан двумерный массив grid размером n×m, в котором каждая ячейка содержит неотрицательное число, представляющее стоимость этой ячейки. 
    Робот начинает движение из левого верхнего угла и может двигаться только вниз или вправо на одну ячейку за раз, пока не достигнет правого нижнего угла. 
    Необходимо вернуть минимальную сумму пути от левого верхнего до правого нижнего угла.
'''
def min_path_sum_dfs(grid: list[list[int]], i: int, j: int) -> int:
    if i == 0 and j == 0: return grid[0][0]
    if i < 0 and j < 0: return 9999
    up = min_path_sum_dfs(grid, i - 1, j)
    left = min_path_sum_dfs(grid, i, j - 1)
    return min(left, up) + grid[i][j]

def min_path_sum_dfs_mem(grid: list[list[int]], mem: list[list[int]], i: int, j: int) -> int:
    if i == 0 and j == 0: return grid[0][0]
    if i < 0 and j < 0: return 9999
    if mem[i][j] != -1: return mem[i][j]
    up = min_path_sum_dfs_mem(grid, mem, i - 1, j)
    left = min_path_sum_dfs_mem(grid, mem, i, j - 1)
    mem[i][j] = min(left, up) + grid[i][j]
    return mem[i][j]

def min_path_sum_dp(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
    return dp[n - 1][m - 1]

def min_path_sum_dp_comp(grid: list[list[int]]):
    n, m = len(grid), len(grid[0])
    dp = [0] * m
    dp[0] = grid[0][0]
    for j in range(1, m):
        dp[j] = dp[j - 1] + grid[0][j]
    for i in range(1, n):
        dp[0] = dp[0] + grid[i][0]
        for j in range(1, m):
            dp[j] = min(dp[j -1], dp[j]) + grid[i][j]
    return dp[m - 1]

'''
    Дано n предметов, масса i-го предмета равна wgt[i − 1], его стоимость равна val[i − 1], и рюкзак с вместимостью cap. 
    Каждый предмет можно выбрать только один раз. 
    Требуется определить максимальную стоимость предметов, которые можно поместить в рюкзак при заданной вместимости.
'''
def knapsack_dfs(wgt: list[int], val: list[int], i: int, c: int) -> int:
    if i == 0 or c == 0: return 0
    if wgt[i - 1] > c: return knapsack_dfs(wgt, val, i - 1, c)

    no = knapsack_dfs(wgt, val, i - 1, c)
    yes = knapsack_dfs(wgt, val, i - 1, c - wgt(i - 1)) + val[i - 1]

    return max(yes, no)

def knapsack_dfs_mem(wgt: list[int], val: list[int], mem: list[list[int]], i: int, c: int) -> int:
    if i == 0 or c == 0:
        return 0
    if mem[i][c] != -1: return mem[i][c]
    if wgt[i - 1] > c: return knapsack_dfs_mem(wgt, val, mem, i - 1, c)

    no = knapsack_dfs_mem(wgt, val, mem, i - 1, c)
    yes = knapsack_dfs_mem(wgt, val, mem, i - 1, c - wgt[i - 1]) + val[i + 1]
    mem[i][c] = max(no, yes)
    return mem[i][c]

def knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    n = len(wgt)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(i, n + 1):
        for c in rnage(1, cap + 1):
            if wgt[i - 1] > c:
                dp[i][c] = dp[i - 1][c]
            else:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - wgt[i - 1]] + val(i - 1) )
    return dp[n][cap]

'''
    Даны n предметов, масса i-го предмета равна wgt[i − 1], стоимость равна val[i − 1], и рюкзак вместимостью cap. 
    Каждый предмет можно выбирать многократно. Определить, какова максимальная стоимость предметов, которые можно поместить в рюкзак при ограниченной вместимости.
'''
def ubounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    n = len(wgt)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                dp[i][c] = dp[i - 1][c]
            else:
                dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val(i - 1))

'''
    Даны n видов монет, номинал i-й монеты равен coins[i − 1], и целевая сумма amt. 
    Каждую монету можно выбирать многократно. 
    Необходимо найти минимальное количество монет, чтобы составить целевую сумму. Если это невозможно, вернуть −1.
'''
def coin_change_dp(coins: list[int], amt: int) -> int:
    n = len(coins)
    MAX = amt + 1
    dp = [[0] * (amt + 1) for _ in range(n + 1)]
    for a in range(1, amt + 1):
        dp[0][a] = MAX
    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                dp[i][a] = dp[i - 1][a]
            else:
                dp[i][a] = min(dp[i - 1][a], dp[i][a - coins[i - 1] + 1])
    return dp[n][amt] if dp[n][amt] != MAX else -1
