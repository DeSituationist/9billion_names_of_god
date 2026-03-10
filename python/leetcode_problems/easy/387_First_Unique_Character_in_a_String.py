class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_ls = list(magazine)
        for char in ransomNote:
            if char not in magazine_ls: return False
            magazine_ls.remove(char)
        return True