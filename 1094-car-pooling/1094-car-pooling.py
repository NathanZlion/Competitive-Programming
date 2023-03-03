class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passangers = [0 for _ in range(1001)]
        
        for trip in trips:
            numPassangers = trip[0]
            from_ = trip[1]
            to_ = trip[2]
            passangers[from_] += numPassangers
            passangers[to_] -= numPassangers
        
        for index in range(1000):
            passangers[index] += passangers[index-1]
        
        for index in range(1000):
            if passangers[index] > capacity:
                return False
        
        return True
