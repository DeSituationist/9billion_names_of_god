from typing import Any
def param_count(*args: Any) -> int:
    return len(args)
print(param_count(1, 2, 3, 4, 5))
print(param_count("hello"))
print(param_count())