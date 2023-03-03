class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passangers = [0 for _ in range(1001)]
        
        for trip in trips:
            if trip[0] > capacity: return False
            passangers[trip[1]] += trip[0]
            passangers[trip[2]] -= trip[0]
        
        for index in range(1000):
            passangers[index] += passangers[index-1]
        
        for index in range(1000):
            if passangers[index] > capacity:
                return False
        
        return True
