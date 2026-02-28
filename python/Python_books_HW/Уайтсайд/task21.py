def fibonacci(sequence_number: int) -> int:
    '''Function that gives fibonacci number on given position'''
    if sequence_number == 0: return 0
    if sequence_number == 1: return 1
    return fibonacci(sequence_number - 1) + fibonacci(sequence_number - 2)
print(fibonacci(4))
print(fibonacci(0))
print(fibonacci(6))