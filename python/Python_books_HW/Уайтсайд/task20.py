def print_triangle(number_of_levels: int, symbol: str) -> None:
    '''Function that prints triangle of given height'''
    for i in range(number_of_levels + 1):
        print((symbol * (2 * i - 1)).center(number_of_levels + 2 * (number_of_levels - 1)))
print_triangle(3, "*")
print_triangle(1, "|")