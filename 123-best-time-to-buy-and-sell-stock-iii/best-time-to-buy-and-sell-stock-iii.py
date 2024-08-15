class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_after_first_buy = float('inf')
        max_profit_after_first_sell = 0
        min_price_after_second_buy = float('inf')
        max_profit_after_second_sell = 0
        
        for price in prices:
            min_price_after_first_buy = min(price, min_price_after_first_buy)
            max_profit_after_first_sell = max(max_profit_after_first_sell, price - min_price_after_first_buy)
            min_price_after_second_buy = min(price - max_profit_after_first_sell, min_price_after_second_buy)
            max_profit_after_second_sell = max(max_profit_after_second_sell, price - min_price_after_second_buy)

        return max_profit_after_second_sell
