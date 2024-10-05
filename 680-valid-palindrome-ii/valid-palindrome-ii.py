class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l + 1] == s[r]:
                    ns = s[l + 1: r + 1]
                    if ns == ns[::-1]:
                        return True
                if s[l] == s[r - 1]:
                    ns = s[l:r]
                    return ns == ns[::-1]

                return False
        
        return True
