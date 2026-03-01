def find_pairs_summing_to_target(input_nums: list[int], target: int) -> list[tuple[int, int]]: 
    '''Return pairs with summ equal to target from list'''
    lenght = len(input_nums)
    return list({(input_nums[x], input_nums[y]) for x in range(lenght) for y in range(lenght) if (input_nums[x] + input_nums[y] == target) and (x != y)})
print(find_pairs_summing_to_target([5, 5, 5, 5], 10))
print(find_pairs_summing_to_target([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(find_pairs_summing_to_target([11, 12, 13, 14, 15], 5))