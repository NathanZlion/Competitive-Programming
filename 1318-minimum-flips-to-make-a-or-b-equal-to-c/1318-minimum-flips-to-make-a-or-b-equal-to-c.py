class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        minFlips = 0
        
        for idx in range(32):
            mask = (1 << idx)
            aPos = 1 if (mask & a) else 0
            bPos = 1 if (mask & b) else 0
            cPos = 1 if (mask & c) else 0

            if cPos:
                if aPos == 0 and bPos == 0:
                    minFlips += 1
            else:
                minFlips += (aPos + bPos)
        
        return minFlips
