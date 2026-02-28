def find_primes(input_nums: list[int]) -> list[int]:
    '''Returns prime numbers from list'''
    return [x for x in input_nums if not any(x % n == 0 for n in list(range(2, x))) and x > 1]
print(find_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_primes([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
print(find_primes([2, 3, 5, 7, 11, 13, 17]))