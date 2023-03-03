class Solution:
    
    def daysNeeded(self, weights, shipCapacity):
        daysTaken = 0
        currWeight = 0
        
        for weight in weights:
            currWeight += weight
            if currWeight > shipCapacity:
                currWeight = weight
                daysTaken += 1

        if currWeight > 0:
            daysTaken += 1

        return daysTaken


    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)-1
        high = sum(weights)+1

        while high > low+1:
            mid = low + (high-low)//2

            if self.daysNeeded(weights, mid) <= days:
                high = mid
            else:
                low = mid

        return high
