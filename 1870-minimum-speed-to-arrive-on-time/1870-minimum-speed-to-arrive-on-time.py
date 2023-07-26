from math import ceil

class Solution:
    
    def hoursSpend(self, dist: List[int], speed: int) -> float:
        """returns from math import ceile hour spent if we move with the given speed"""
        hour = 0.0
        for d_index in range(len(dist)-1):
            distance = dist[d_index]
            hour += ceil(distance/speed)

        last_dist = dist[-1]
        hour += last_dist/speed

        return hour

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 0            # not fast enough speeds
        right = 10**7 + 1   # fast enough speeds
        
        while right > left + 1:
            mid= (left + right) // 2
            if self.hoursSpend(dist, mid) > hour:
                left=mid
            else:
                right = mid            

        return right if right != 10**7+1 else -1
