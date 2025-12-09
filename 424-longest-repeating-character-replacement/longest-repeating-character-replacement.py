from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        counts = defaultdict(int)
        max_char = 0
        l = 0
        found_max = 0

        


        for r, c in enumerate(s):
            counts[c] += 1
            max_char = max(max_char, counts[c])

            while r - l + 1 > max_char + k:
                counts[s[l]] -= 1
                l += 1

            found_max = max(found_max, r - l + 1)

        return found_max