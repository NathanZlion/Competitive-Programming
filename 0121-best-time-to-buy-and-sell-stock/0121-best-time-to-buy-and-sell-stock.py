class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_sofar = prices[0]
        max_profit = 0
        
        for index in range(1, len(prices)):
            curr_price = prices[index]
            max_profit_if_sold_now = curr_price - min_price_sofar
            max_profit = max(max_profit, max_profit_if_sold_now)
            min_price_sofar = min(min_price_sofar, curr_price)

        return max_profit
