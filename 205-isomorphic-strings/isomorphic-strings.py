class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hp = {}
        mapped = set()
        for i, c in enumerate(s):
            if c in hp:
                if t[i] != hp[c]:
                    return False
            else:
                if t[i] in mapped:
                    return False
                hp[c] = t[i]
                mapped.add(t[i])

        return True
