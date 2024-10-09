class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        max_len = 0
        start = 0


        for i in range(len(s)):
            if char_idx.get(s[i], -1) >= start:
                start = char_idx[s[i]] + 1
                char_idx[s[i]]= i
            else:
                max_len = max(max_len, i - start + 1)
                char_idx[s[i]]= i


        return max_len 