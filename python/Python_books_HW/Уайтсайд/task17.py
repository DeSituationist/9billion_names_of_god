def check_if_string_is_happy(input_str: str) -> bool:
    '''Function that returns True if there are no repeats in slices of length 3'''
    result = []
    for i in range(0, len(input_str)):
        sl = input_str[i:i+3]
        if len(sl) < 3: break
        result.append(all(sl.count(ch) == 1 for ch in sl))
    return all(check == True for check in result)
print(check_if_string_is_happy("abcdefg"))
print(check_if_string_is_happy("abcabcabcabc"))
print(check_if_string_is_happy("hello"))