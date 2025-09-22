from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_char = 0
        l = 0
        max_len = 0

        for r, c in enumerate(s):
            count[c] += 1
            max_char = max(max_char, count[c])

            while r - l + 1 > max_char + k:
                count[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            # print("l r", l, r, max_len)

        return max_len