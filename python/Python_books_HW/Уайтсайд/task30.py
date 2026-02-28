def find_zero_sum_triplets(input_nums: list[int]) -> list[tuple[int, int, int]]:
    '''Finds groups of three numbers summ of which equals zero'''
    if all(num > 0 for num in input_nums): return []
    lenght = len(input_nums)
    answer = []
    for i in range(lenght):
        if input_nums[i] > 0: continue
        else:
            for k in range(lenght):
                for j in range(k + 1, lenght):
                    if input_nums[k] + input_nums[j] == -input_nums[i]:
                        answer.append((k, j, i))
    return answer
print(find_zero_sum_triplets([1, 2, 3, 4, 5]))
print(find_zero_sum_triplets([1, 2, 3, 4, 5, -9]))
print(find_zero_sum_triplets([1, 2, 3, 4, 5, -9, -9]))