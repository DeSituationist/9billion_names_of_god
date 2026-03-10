class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if ((word.upper() == word) or (word.capitalize()) == word or (word.lower() == word)) else False