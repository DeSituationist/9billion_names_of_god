def longestPalindrome(s: str) -> int:
    chars_bt = [s.count(char) for char in set(s) if s.count(char) % 2 == 0]
    chars_nbt = [s.count(char) for char in set(s) if s.count(char) % 2 != 0]
    sm = sum(chars_bt) if len(chars_bt) > 0 else 0
    sm_nbt, mx_nbt = 0, 0
    if len(chars_nbt) > 0: 
        mx_nbt = max(chars_nbt)
        chars_nbt.remove(mx_nbt)
    for cnt in chars_nbt:
        sm_nbt += (cnt - 1)
    return sm + mx_nbt + sm_nbt
print(longestPalindrome("ccc"))