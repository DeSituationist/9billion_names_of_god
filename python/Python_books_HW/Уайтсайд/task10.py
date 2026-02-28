def get_second_largest_number(input_nums: list[int]) -> int | None:
    '''Function that returns second largest number in list'''
    return sorted(input_nums)[-2] if len(input_nums) > 1 else None
print(get_second_largest_number([1, 2, 3, 4, 5]))
print(get_second_largest_number([3, 45, 345, 435, 345, 43, 56, 34, 234, 34]))
print(get_second_largest_number([1]))