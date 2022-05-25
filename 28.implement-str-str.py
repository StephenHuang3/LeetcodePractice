#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        nlen = len(needle)
        hlen = len(haystack)

        found = True

        for i in range(hlen):
            for j in range(nlen):
                if i + j >= hlen:
                    found = False
                    break
                elif haystack[i + j] == needle[j]:
                    continue
                else:
                    found = False
                    break
            if found:
                return i
            found = True

        return -1


# @lc code=end
