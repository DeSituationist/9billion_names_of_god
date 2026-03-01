def insertion_sort(input_nums: list[int]) -> list[int]:
    '''Sorts given list'''
    for i in range(len(input_nums)):
        for j in range(i + 1, len(input_nums)):
            if input_nums[j] < input_nums[i]:
                temp = input_nums[i] 
                input_nums[i] = input_nums[j]
                input_nums[j] = temp
    return input_nums
print(insertion_sort([5, 10, 9, 11, 4]))
print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([-1, -2, -3, -4, -5]))