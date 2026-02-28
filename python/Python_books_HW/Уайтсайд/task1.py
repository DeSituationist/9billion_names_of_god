def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    '''Function that filters strs with "a" in them'''
    return [s for s in input_strs if 'a' in s]
print(filter_strings_containing_a(["apple", "banana", "cherry", "date"]))