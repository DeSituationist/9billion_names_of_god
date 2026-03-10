class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        return True if str_num == str_num[::-1] else False