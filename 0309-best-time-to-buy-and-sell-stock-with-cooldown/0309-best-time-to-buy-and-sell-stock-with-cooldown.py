class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        numDays = len(prices)
        
        buy, sell, cooldown = -prices[0], 0, 0  
        
        for i in range(1, numDays):
            _buy = max(buy, cooldown - prices[i])  
            _sell = max(sell, buy + prices[i])
            _cooldown = max(cooldown, sell)
            buy, sell, cooldown = _buy, _sell, _cooldown
        
        return max(sell, cooldown)
