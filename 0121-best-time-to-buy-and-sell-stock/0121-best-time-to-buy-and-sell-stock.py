class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for index in range(1, len(prices)):
            curr_price = prices[index]
            min_price = min(min_price, curr_price)
            max_profit = max(max_profit, curr_price - min_price)

        return max_profit
