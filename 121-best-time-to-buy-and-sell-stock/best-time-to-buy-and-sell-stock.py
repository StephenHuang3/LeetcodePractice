class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        min_price = float("infinity")

        for r in range(len(prices)):
            if prices[r] < min_price:
                min_price = prices[r]
            else:
                max_profit = max(max_profit, prices[r] - min_price)

        return max_profit