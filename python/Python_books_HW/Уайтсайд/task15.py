def filter_palindromes(input_strs: list[str]) -> list[str]:
    '''Function returns list of string that are plaindromes'''
    return [s for s in input_strs if s == s[::-1]]
print(filter_palindromes(["cat", "dog", "racecar", "deified", "giraffe"]))
print(filter_palindromes(["kayak", "deified", "rotator", "repaper", "deed","a"]))
print(filter_palindromes(["ab", "ba", "cd", "ef", "pt"]))