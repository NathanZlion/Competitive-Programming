class Solution:
    def getSlope(self, coordinate1, coordinate2) -> Optional[float] :
        x1, y1 = coordinate1
        x2, y2 = coordinate2
        if x2 == x1:
            return inf
        
        return (y2 - y1) / (x2 - x1)

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        slope = self.getSlope(coordinates[0], coordinates[1])
        n = len(coordinates)
        for i in range(n-1):
            if self.getSlope(coordinates[i], coordinates[i+1]) != slope:
                return False
        
        return True