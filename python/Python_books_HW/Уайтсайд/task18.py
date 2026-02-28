def get_number_of_digits(input_num: int, counter = 0) -> int:
    '''Recursive function that doesnt turn int into str and gives number of digits'''
    while input_num > 0:
        return get_number_of_digits(input_num//10, counter + 1)
    return counter
print(get_number_of_digits(1234))
print(get_number_of_digits(0))
print(get_number_of_digits(123456789))