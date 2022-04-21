#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        count = 0

        negative = False

        if (dividend < 0 and divisor > 0) :
            dividend *= -1
            negative = True
        
        if (dividend >= 0 and divisor < 0) :
            divisor *= -1
            negative = True

        if(dividend < 0 and divisor < 0) :
            divisor *= -1
            dividend *= -1

        while (dividend >= divisor):
            count += 1
            dividend -= divisor
        
        if(negative):
            count *= -1

        if (negative == False):
            if (count == 2**31):
                return 2**31-1

        return count;
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
# @lc code=end

