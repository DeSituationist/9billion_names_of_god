from typing import Any
def rotate_list_left(input_list: list[Any], rotate_amount: int) -> list[Any]:
    '''Function that rotates list through left side'''
    return [input_list[(i+rotate_amount) % len(input_list)] for i in range(len(input_list))]
print(rotate_list_left([1, 2, 3, 4, 5], 2))
print(rotate_list_left([1, 2, 3, 4, 5], 5))
print(rotate_list_left([1, 2, 3, 4, 5], 7))