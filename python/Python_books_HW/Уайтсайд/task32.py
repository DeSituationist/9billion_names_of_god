def contains_python_chars(input_str: str) -> bool:
    '''Checks if there is python in str'''
    return True if input_str.lower() == 'python' or input_str.lower() == 'nohtyp' else False
print(contains_python_chars("pYThon"))
print(contains_python_chars("Nohtyp"))
print(contains_python_chars("pythZon"))