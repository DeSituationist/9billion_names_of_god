class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {')': '(', ']': '[', '}': '{'}
        parantheses = []
        for ch in s:
            if ch in brackets_map:                
                if not parantheses or parantheses[-1] != brackets_map[ch]:
                    return False
                parantheses.pop()
            else:                             
                parantheses.append(ch)
        if len(parantheses) != 0: return False
        return True