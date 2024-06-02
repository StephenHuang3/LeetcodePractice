class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for c in magazine:
            mag[c] = 1 + mag.get(c, 0)

        for c in ransomNote:
            if c not in mag:
                return False
            else:
                if mag[c] == 0:
                    return False
                mag[c] -= 1
        
        return True

        