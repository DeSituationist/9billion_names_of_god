class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(set(nums), reverse = True)
        lenght = len(nums)
        if lenght >= 3: return nums[2]
        else: return nums[0]