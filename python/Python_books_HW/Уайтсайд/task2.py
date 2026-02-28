def sum_if_less_than_fifty(num_one: int, num_two: int) -> int | None:
    '''Function that returns summ if summ < 50 else returns None'''
    sum = num_one + num_two
    return sum if sum < 50 else None
print(sum_if_less_than_fifty(20, 20))
print(sum_if_less_than_fifty(20, 30))