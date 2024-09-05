class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [0] * len(prices)

        for i in range(k):
            pos = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, prices[i] + pos)
                dp[i] = profit

        return dp[-1]

