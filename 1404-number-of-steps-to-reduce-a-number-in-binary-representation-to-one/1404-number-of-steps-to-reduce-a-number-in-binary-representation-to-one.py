class Solution:
    def numSteps(self, s: str) -> int:
        integer = int(s, 2)
        ops = 0

        while integer != 1:
            # it's odd
            if integer & 1:
                integer += 1
            else:
                integer >>= 1

            ops += 1
        
        return ops