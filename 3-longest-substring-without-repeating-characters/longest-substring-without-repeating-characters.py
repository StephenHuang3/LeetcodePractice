class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        cur_max = 0
        l = 0
        for r in range(len(s)):
            if s[r] in cur:
                while s[l] != s[r]:
                    cur.remove(s[l])
                    l += 1
                l += 1
            else:
                cur.add(s[r])
            cur_max = max(cur_max, r - l + 1)

        return cur_max