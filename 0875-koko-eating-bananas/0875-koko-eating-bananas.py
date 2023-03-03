class Solution:
    
    def timeTaken(self, piles, atOnce):
        time = 0
        
        for pile in piles:
            time +=  math.ceil(pile/atOnce)

        print(atOnce, time)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles)+1
        
        while high > low+1:
            mid = (low + high)//2

            if self.timeTaken(piles, mid) > h:
                low = mid
            else:
                high = mid

        return high