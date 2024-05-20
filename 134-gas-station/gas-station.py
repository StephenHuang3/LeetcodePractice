class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        travel = []
        sum = 0
        for i in range(len(gas)):
            difference = gas[i] - cost[i]
            travel.append(difference)
            sum += difference
        if sum < 0:
            return -1
        
        sum = 0
        start = -1
        for i in range(len(travel)):
            sum += travel[i]
            if sum >= 0 and start == -1:
                start = i
            elif sum <0:
                start = -1
                sum = 0

        return start

            
        