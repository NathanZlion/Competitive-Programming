class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #edge case
        if len(days) == 0:
            return 0 

        self.oneDayPass, self.sevenDayPass, self.thirtyDayPass = costs
        buying_days = set(days)

        @cache
        def dp(day):
            if day > days[-1]:
                return 0

            oneDayCost = dp(day + 1) + self.oneDayPass
            sevenDayCost = dp(day + 7) + self.sevenDayPass
            thirtyDayCost = dp(day + 30) + self.thirtyDayPass
            efficientCost = min(oneDayCost, sevenDayCost, thirtyDayCost)  

            if day in buying_days:
                return efficientCost 

            return min(dp(day + 1), efficientCost)

        return dp(days[0])
