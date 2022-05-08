#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        inrpos = 0
        possible = True


        for initpos in range(len(gas)):
            for i in range(len(gas)):
                if (i + initpos >= len(gas)):
                    inrpos = i + initpos - len(gas)
                else:
                    inrpos = i + initpos
                    
                tank += gas[inrpos]
                tank -= cost[inrpos]

                if tank < 0:
                    possible = False
                    break
            
            if possible:
                return initpos

            possible = True
            tank = 0


        return -1

        
# @lc code=end

