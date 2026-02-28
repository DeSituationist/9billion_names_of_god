def get_longest_string(input_strs: list[str]) -> str:
    '''Function that returns longest str in list'''
    return max(input_strs, key=len)
print(get_longest_string(["cat", "dog", "bird", "lizard"]))
print(get_longest_string(["cat", "dog", "bird", "wolf"]))
print(get_longest_string(["a", "b", "c", "d"]))