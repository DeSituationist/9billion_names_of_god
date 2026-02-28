tap_code_map = {
"a": ". .",
"b": ". ..",
"c": ". ...",
"d": ". ....",
"e": ". .....",
"f": ".. .",
"g": ".. ..",
"h": ".. ...",
"i": ".. ....",
"j": ".. .....",
"l": "... .",
"m": "... ..",
"n": "... ...",
"o": "... ....",
"p": "... .....",
"q": ".... .",
"r": ".... ..",
"s": ".... ...",
"t": ".... ....",
"u": ".... .....",
"v": "..... .",
"w": "..... ..",
"x": "..... ...",
"y": "..... ....",
"z": "..... .....",
}
def tap_code_to_english(input_code: str) -> str:
    '''Function that translates taps to english'''
    reverse_dict = {v: k for k, v in tap_code_map.items()}
    words = input_code.split('   ')
    characters = [word.split('  ') for word in words]
    result = ''
    for i in characters:
        for x in i:
            if x == '': continue
            result += reverse_dict[x]
        result += ' '
    return result
print(tap_code_to_english(".. ...  .. ....   .. ...  .. ...."))
print(tap_code_to_english(". ...  ... ....  ... ....  ... ."))
print(tap_code_to_english(""))