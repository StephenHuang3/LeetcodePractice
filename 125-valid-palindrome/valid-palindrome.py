import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.upper()
        print(s)
        n = len(s) - 1
        for i in range(len(s) // 2):
            if s[i] != s[n - i]:
                return False
        return True