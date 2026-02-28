from typing import Any
def my_zip(input_list_a: list[Any], input_list_b: list[Any]) -> list[tuple[Any, Any]]:
    '''Function that copies in-built zip() function'''
    return [(input_list_a[i], input_list_b[i]) for i in range(min(len(input_list_a), len(input_list_b)))]
print(my_zip([1, 2, 3, 4], [5, 6, 7, 8]))
print(my_zip([], []))
print(my_zip([1, 2, 3], [5, 6, 7, 8]))