#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        toRoman(num)
    
    def toRoman(k):
        if (k >= 1):
            return "I" + toRoman(k-1)

        else:
            return ""
        
# @lc code=end

