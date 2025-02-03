class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        max_profit = 0
        lowest_price = prices[0]

        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - lowest_price)
            lowest_price = min(lowest_price, prices[i])

        return max_profit