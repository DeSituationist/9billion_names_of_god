def sum_even(input_nums: list[int]) -> int:
    '''Function that returns summ of even numbers in list'''
    return sum(x for x in input_nums if x % 2 == 0)
print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even([10, 20, 30, 40, 50]))
print(sum_even([9, 7, 5, 3, 1]))