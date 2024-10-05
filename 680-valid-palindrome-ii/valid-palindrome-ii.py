class Solution:
    def validPalindrome(self, s: str) -> bool:
        breakpoint = -1
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                breakpoint = i
                break
        
        if breakpoint == -1:
            return True

        found_left = True
        found_right = True

        for i in range(breakpoint, len(s) // 2):
            if s[i + 1] != s[-i - 1]:
                found_left = False
                break
        
        if found_left:
            return True

        for i in range(breakpoint, len(s) // 2):
            if s[i] != s[-i - 2]:
                found_right = False
                break
        
        return found_left or found_right
