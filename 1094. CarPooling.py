class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        count = Counter()
        for numOfPassengers, start, end in trips:
            count[start] += numOfPassengers
            count[end] -= numOfPassengers
        
        currPassangersSum = 0
        for i,j in sorted(count.items()):
            currPassangersSum += j
            if currPassangersSum > capacity:
                return False
        return True
