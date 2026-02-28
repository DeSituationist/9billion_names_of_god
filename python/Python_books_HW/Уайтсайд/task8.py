def filter_type_str(input_list: list[str | int]) -> list[str]:
    '''Functions that returns strings from list'''
    return [i for i in input_list if type(i) == str]
print(filter_type_str(["hello", 1, 2, "www"]))
print(filter_type_str([]))
print(filter_type_str([1, 2, 3, 4, 5]))