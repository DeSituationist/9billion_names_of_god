class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, reverse = True)
        res, cur_check = '', ''
        for char in strs[0]:
            cur_check += char
            if all(string.startswith(cur_check) for string in strs): 
                res += char