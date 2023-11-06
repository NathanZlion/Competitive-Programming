class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = inf
        
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit