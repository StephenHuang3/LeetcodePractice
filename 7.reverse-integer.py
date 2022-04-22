#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        letters = ""

        negative = False

        if (x == 0):
            return 0

        if (x < 0):
            negative = True
            x *= -1
    
        while (x % 10 == 0):
            x = int(x / 10)
            continue;
            
        while(x != 0):                
            letters = letters + str(x % 10)
            
            x = int(x / 10)
            
        if(int(letters) > 2 ** 31 - 1 or int(letters) < -(2 ** 31)):
            return 0;
        
        if(negative) :
            return "-" + letters
        
        return letters
        
# @lc code=end

