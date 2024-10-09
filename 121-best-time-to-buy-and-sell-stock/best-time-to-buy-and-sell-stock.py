class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        cur_profit = 0

        for r in range(len(prices)):
            cur_profit = prices[r] - prices[l]
            if cur_profit < 0:
                l = r
                cur_profit = 0
            else:
                max_profit = max(max_profit, cur_profit)

        return max_profit
