def binary_search(sorted_list: list[int], value_to_find: int) -> int:
    '''Binary search'''
    cur_lst = sorted_list[::]
    while len(cur_lst) > 0:
        midd = None
        if len(cur_lst) % 2 == 0: midd = len(cur_lst) // 2 - 1
        else: midd = len(cur_lst) // 2
        if cur_lst[midd] == value_to_find: 
            return sorted_list.index(cur_lst[midd])  
        else:
            if value_to_find < cur_lst[midd]: cur_lst = cur_lst[:midd]
            else: cur_lst = cur_lst[midd+1:]
    return -1
searchable_list = [2, 3, 4, 10, 40]
print(binary_search(searchable_list, 10))
print(binary_search(searchable_list, 0))
print(binary_search([], 0))