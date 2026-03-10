import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(sum(int(num1[i]) * 10 **(len(num1) - (i + 1)) for i in range(len(num1))) + sum(int(num2[j]) * 10 **(len(num2) - (j + 1)) for j in range(len(num2))))