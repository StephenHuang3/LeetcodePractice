class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(cost))]
        cur = 0
        start = 0
        if sum(diff) < 0:
            return -1

        for i in range(len(gas)):
            cur += diff[i]
            if cur < 0:
                start = i + 1
                cur = 0

        return start