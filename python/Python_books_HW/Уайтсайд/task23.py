def xor(input_a: str, input_b: str) -> str:
    '''Function that xors given string into one'''
    return ''.join(['1' if (input_a[i] != input_b[i]) else '0' for i in range(min(len(input_a), len(input_b)))])
print(xor("1111", "1111"))
print(xor("1111", "0000"))
print(xor("1101", "00010"))