class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        previous_checker, cur_checker = num + 1, num
        while cur_checker < previous_checker:
            previous_checker = cur_checker
            cur_checker = (cur_checker + num // cur_checker)//2
        return cur_checker * cur_checker == num