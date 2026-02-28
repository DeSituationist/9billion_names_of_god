def filter_strings_with_vowels(input_strs: list[str]) -> list[str]:
    '''Function that returns strings with at least one vowel in it'''
    vowels = 'AEIOUaeiou'
    return [s for s in input_strs if len([x for x in s if x in vowels]) > 0]
print(filter_strings_with_vowels(["apple", "banana", "zyxvb"]))
print(filter_strings_with_vowels([]))
print(filter_strings_with_vowels(["q", "w", "e", "r", "t", "y"]))