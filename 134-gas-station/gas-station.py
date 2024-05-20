class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        total = 0
        start = -1

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = -1
                total = 0
                continue
            elif total >=0 and start == -1:
                start = i
        
        return start
            

            
        