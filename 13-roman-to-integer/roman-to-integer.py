class Solution:
    def romanToInt(self, s: str) -> int:
        hp = {}
        hp["I"] = 1
        hp["V"] = 5
        hp["X"] = 10
        hp["L"] = 50
        hp["C"] = 100
        hp["D"] = 500
        hp["M"] = 1000
        total = 0
        c = 0

        while c < len(s):
            if c + 1 < len(s) and hp[s[c]] < hp[s[c + 1]]:
                total += hp[s[c + 1]] - hp[s[c]]
                c += 2
            else:
                total += hp[s[c]]
                c += 1


        return total
        