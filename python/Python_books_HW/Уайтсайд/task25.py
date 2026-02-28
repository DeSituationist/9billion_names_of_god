def is_valid_equation(input_equation: str) -> bool:
    '''Function that checks if equation is correct'''
    input_equation = input_equation.replace('=', '==')
    return eval(input_equation)
print(is_valid_equation("2 + 3 = 5"))
print(is_valid_equation("-5 + -6 = -11"))
print(is_valid_equation("-2 + 3 = -5"))