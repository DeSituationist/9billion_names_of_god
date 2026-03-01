def rot13(input_str: str) -> str:
    '''Encrypts given string'''
    result = ''
    for ch in input_str:
        if 65<=ord(ch)<=90:
            result += chr((ord(ch) - 65 - 13)%26 + 65)
        elif 97<=ord(ch)<=122:
            result += chr((ord(ch) - 97 - 13)%26 + 97)
        else:
            result += ch
    return result
print(rot13("Hello world!"))
print(rot13("Cool puzzles!"))
print(rot13("12345!@£$%"))