class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c = 0
        total = 0

        for bracket in s:
            if bracket == "(":
                c += 1
            if bracket == ")":
                if c == 0:
                    total += 1
                else:
                    c -= 1

        return total + c
        