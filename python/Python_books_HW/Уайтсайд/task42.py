def bitwise_add(num_one: int, num_two: int) -> int:
    '''Returns summ of numbers using only bytewise operands'''
    if num_one > 0 and num_two > 0: return num_one ^ num_two
    else: return -((-num_one) ^ (-num_two))
print(bitwise_add(3, 4))
print(bitwise_add(255, 256))
print(bitwise_add(-1, -2))