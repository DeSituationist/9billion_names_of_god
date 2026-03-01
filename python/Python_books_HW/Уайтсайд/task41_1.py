roman_map = {
    1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
    90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",
    4: "IV", 1: "I"
}
reverse_roman_map = {k: v for v, k in roman_map.items()}
def int_to_roman(input_nums: int) -> str:
    '''Truns integer into roman version'''
    result = []
    while input_nums > 0:
        closest = -1000
        for ky in roman_map.keys():
            if input_nums - ky >= 0 and ky > closest: closest = ky
        result.append(roman_map[closest])
        input_nums -= closest
    return ''.join(result)
def roman_to_int(to_convert: str) -> int:
    '''Converts roman numbers to modern ones'''
    result = 0
    while to_convert != '':
        if len(to_convert) >= 2 and to_convert[:2] in reverse_roman_map.keys():
            result += reverse_roman_map[to_convert[:2]]
            to_convert = to_convert[2:]
        elif to_convert[0] in reverse_roman_map.keys():
            result += reverse_roman_map[to_convert[0]]
            to_convert = to_convert[1:]
    return result
def converter(given: int | str) -> None:
    if type(given) == int: print(int_to_roman(given))
    else: print(roman_to_int(given))
converter(4)
converter(27)
converter(4999)
converter('XXVII')
converter('IV')
converter('MMMMCMXCIX')