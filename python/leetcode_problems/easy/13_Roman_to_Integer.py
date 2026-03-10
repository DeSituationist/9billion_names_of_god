class Solution:
    def romanToInt(self, s: str) -> int:
        romans_map = {
            'I': 1,
            'Z': 4,
            'V': 5,
            'F': 9,
            'X': 10,
            'E': 40,
            'L': 50,
            'G': 90,
            'C': 100,
            'O': 400,
            'D': 500,
            'K': 900,
            'M': 1000,
        }
        sp_map = {
            'IV': 'Z', 
            'IX': 'F', 
            'XL': 'E', 
            'XC': 'G', 
            'CD': 'O', 
            'CM': 'K',
        }
        def change_specials(s):
            for old, new in sp_map.items():
                s = s.replace(old, new)
            return s
        if any(key in s for key in sp_map.keys()):
            s = change_specials(s)
        return sum(romans_map[roman] for roman in s)