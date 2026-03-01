roman_map = {
    1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
    90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",
    4: "IV", 1: "I"
}
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
print(int_to_roman(4))
print(int_to_roman(27))
print(int_to_roman(4999))