#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for r in range(numRows)]
        count = 0

        while count < len(s):
            for i in range(numRows):
                rows[i].append(s[count])
                count += 1
                if count == len(s):
                    break

            if count == len(s):
                break

            for i in range(numRows - 2, 0, -1):
                rows[i].append(s[count])
                count += 1
                if count == len(s):
                    break

        return "".join(["".join(r) for r in rows])


# @lc code=end
