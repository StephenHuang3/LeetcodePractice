#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        count = 0
        for i in range(len(s)):
            if count >= len(p):
                return False
            elif s[i] == p[count]:
                count += 1
                continue
            elif p[count] == "?":
                count += 1
                continue
            elif p[count] == "*":
                count += 1
                while count < len(p) and i < len(s):
                    if s[i] == p[count]:
                        count += 1
                        i += 1
                        if i == len(s):
                            return True
                        break
                    else:
                        i += 1
                if p[len(p) - 1] == "*":
                    return True
                continue

            else:
                return False

        if count != len(p):
            return False

        return True


# @lc code=end
