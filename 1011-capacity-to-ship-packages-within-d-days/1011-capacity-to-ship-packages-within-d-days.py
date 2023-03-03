class Solution:
    
    def daysNeeded(self, weights, shipCapacity, maxDays):
        daysTaken = 0
        currWeight = 0
        
        for weight in weights:
            currWeight += weight
            if currWeight > shipCapacity:
                currWeight  = weight
                daysTaken += 1

        if currWeight > 0:
            daysTaken += 1

        return daysTaken <= maxDays


    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)-1
        high = sum(weights)+1 # take all at once

        while high > low+1:
            mid = low + (high-low)//2
            isAllowed = self.daysNeeded(weights, mid, days)

            if isAllowed:
                high = mid
            else:
                low = mid

        return high
