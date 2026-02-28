def ascii_to_string(input_ascii_codes: list[int]) -> str:
    '''Function that returns string from ascii codes'''
    return ''.join(chr(x) for x in input_ascii_codes)
print(ascii_to_string([80, 114, 111, 103, 114, 97, 109, 109, 105,
110, 103, 32, 112, 117, 122, 122, 108, 101, 115, 33]))
print(ascii_to_string([]))
print(ascii_to_string([97, 65]))