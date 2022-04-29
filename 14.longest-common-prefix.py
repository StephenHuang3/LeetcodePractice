#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        count = 0
        
        min = 99999
        
        for e in strs:
            if(len(e) < min):
                min = len(e)

        for x in range(min):
            letter = strs[0][count]
            for e in strs:
                if (letter != e[count]):
                    return strs[0][0:count]
            count += 1

        return strs[0][0:count]
        
# @lc code=end

