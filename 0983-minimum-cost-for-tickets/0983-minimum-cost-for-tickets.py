class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #edge case
        if len(days) == 0:
            return 0 

        self.oneDayPass, self.sevenDayPass, self.thirtyDayPass = costs
        buying_days = set(days)
        
        dp = [None] * (days[-1] + 31)
        for i in range(30):
            dp[i] = 0

        for i in range(30, len(dp)):
            onedayCost = self.oneDayPass + dp[i-1]
            sevendayCost = self.sevenDayPass + dp[i - 7]
            thirtydayCost = self.thirtyDayPass + dp[i - 30]
            
            dp[i] = min(onedayCost, sevendayCost, thirtydayCost)
            if i - 30 not in buying_days:
                dp[i] = min(dp[i - 1],dp[i])
        
        return dp[-1]