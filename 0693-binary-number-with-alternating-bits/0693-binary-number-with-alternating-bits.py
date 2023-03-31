class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        lastBit = 1 if n%2 else 0
        
        while n:
            if n%2 != lastBit:
                return False
            n >>= 1
            lastBit = 0 if lastBit else 1

        return True
        
        