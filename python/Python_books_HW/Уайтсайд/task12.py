def string_to_ascii(input_str: str) -> list[int]:
    '''Function that returns ascii codes of chars in string'''
    return [ord(x) for x in input_str]
print(string_to_ascii("Programming puzzles!"))
print(string_to_ascii(""))
print(string_to_ascii("aA"))