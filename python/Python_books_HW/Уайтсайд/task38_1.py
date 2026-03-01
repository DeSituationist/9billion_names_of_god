def find_pairs_summing_to_target(input_nums: list[int], target: int) -> list[tuple[int, int]]: 
    '''Return pairs with summ equal to target from list'''
    pairs = set()
    for i, num in enumerate(input_nums):
        if (target - num) in input_nums and i != input_nums.index(target - num):
            pairs.add((min(num, target-num), max(num, target-num)))
    return pairs
print(find_pairs_summing_to_target([5, 5, 5, 5], 10))
print(find_pairs_summing_to_target([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(find_pairs_summing_to_target([11, 12, 13, 14, 15], 5))