def gcd(num_one: int, num_two: int) -> int:
    '''Finds gcd for two numbers'''
    return max([x for x in range(1, (max(num_one, num_two)//2)) if num_one % x == 0 and num_two % x == 0])
print(gcd(36, 8))
print(gcd(5, 25))
print(gcd(5, 26))