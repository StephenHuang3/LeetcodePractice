class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s, fudge):
            if len(s) <= 1:
                return True
            elif s[0] == s[-1]:
                return valid(s[1:-1], fudge)
            elif fudge == 1:
                return False
            else:
                return valid(s[:-1], 1) or valid(s[1:], 1)


        return valid(s, 0)