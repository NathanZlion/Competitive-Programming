class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        hammingDistance = 0
        
        while x or y:
            hammingDistance += 1 & (x ^ y)
            x>>=1
            y>>=1


        return hammingDistance
