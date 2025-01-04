class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        max_profits = [0]
        max_profit_ends = [-1]

        sorted_indexes = [index for index in range(len(endTime))]
        sorted_indexes.sort(key = lambda x: endTime[x])

        for i in sorted_indexes:
            available = bisect.bisect_right(max_profit_ends, startTime[i]) - 1

            if max_profits[-1] < profit[i] + max_profits[available]:
                max_profits.append(profit[i] + max_profits[available])
                max_profit_ends.append(endTime[i])

        return max_profits[-1]