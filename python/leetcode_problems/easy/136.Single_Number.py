class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return sorted(nums, key=nums.count)[0]