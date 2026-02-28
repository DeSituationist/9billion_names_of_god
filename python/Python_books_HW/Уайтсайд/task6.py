def filter_even_length_strings(input_strs: list[str]) -> list[str]:
    '''Function that returns strings with even length'''
    return [s for s in input_strs if len(s) % 2 == 0]
print(filter_even_length_strings(["cat", "dog", "fish", "elephant"]))
print(filter_even_length_strings(["q", "w", "e", "r", "t", "y"]))
print(filter_even_length_strings(["qq", "ww", "ee", "rr", "t", "yy"]))