from typing import Any
def my_zip_one(*input_lists: list[Any]) -> list[tuple[Any, ...]]:
    '''Function that copies in-built zip() function for any args'''
    result = []
    for elem in range(min(len(lst) for lst in input_lists)):
        tupl = []
        for lst in input_lists:
            tupl.append(lst[elem])
        result.append(tuple(tupl))
    return result
print(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))
print(my_zip_one([1, 2, 3], [5, 6, 7, 8]))
print(my_zip_one([], []))