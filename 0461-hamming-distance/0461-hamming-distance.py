class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        hammingDistance = 0
        
        while x>0 and y>0:
            hammingDistance += 1 & (x ^ y)
            x>>=1
            y>>=1
        
        
        hammingDistance += x.bit_count()
        hammingDistance += y.bit_count()
        
        return hammingDistance
        
            
        