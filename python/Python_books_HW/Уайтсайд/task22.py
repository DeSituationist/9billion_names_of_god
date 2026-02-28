def harmonic_sum(n : int) -> float:
    '''Function that gives summ of harmonic row'''
    if n == 1: return 1
    if n == 0: return 0
    return 1 / n + harmonic_sum(n - 1)
print(harmonic_sum(5))
print(harmonic_sum(2))
print(harmonic_sum(0))