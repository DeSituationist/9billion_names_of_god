def censor_python(input_strs: list[str]) -> list[str]:
    censor_list = 'PYTHONpython'
    return [''.join(['X' if x in censor_list else x for x in list(s)]) for s in input_strs]
print(censor_python(["python", "hello", "HELLO"]))
print(censor_python(["abcdefg"]))
print(censor_python([]))