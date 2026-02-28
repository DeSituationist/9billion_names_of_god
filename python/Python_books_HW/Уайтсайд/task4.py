def remove_vowels(input_str: str) -> str:
    '''Function that returns str without vowels'''
    vowels = 'AEIOUYaeiouy'
    return ''.join([x for x in input_str if x not in vowels])
print(remove_vowels("Hello, World!"))
print(remove_vowels("aeiouAEIOU"))
print(remove_vowels("zzxxxccvvvbbnnmmmLLKKJJHH"))