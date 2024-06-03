class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        hp = {}
        mapped = set()
        if len(pattern) != len(arr): return False

        for i, c in enumerate(pattern):
            if c not in hp:
                if arr[i] in mapped:
                    return False
                hp[c] = arr[i]
                mapped.add(arr[i])
            else:
                if hp[c] != arr[i]:
                    return False

        return True