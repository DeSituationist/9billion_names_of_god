def get_parentheses_groups(input_str: str) -> list[str]:
    '''Splits theses into groups'''
    group = ''
    result = []
    for elem in input_str:
        if elem == '(' and (group == '' or ')' not in group): group += '('
        if elem == ')' and group.count('(') > group.count(')'): group += ')'
        if group.count('(') == group.count(')') and len(group) != 0:
            result.append(group)
            group = ''
    return result
print(get_parentheses_groups("(( )) (( ) ) ( (( )))"))
print(get_parentheses_groups("( ( ( ( ( ( ( ) ) ) ) ) ) )"))
print(get_parentheses_groups(""))