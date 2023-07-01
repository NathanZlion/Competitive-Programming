class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        mask = 1
        limit = 2**32
        solution = 0
        
        while mask < limit:
            onesCount = 0
            
            for num in nums:
                onesCount += (num & mask)
            
            # if count is a multiple of 3
            if (onesCount % 3):
                solution |= mask # flip on that bit

            mask <<= 1
        
        # if sign bit is on (is negative)
        if solution & (1 << 31):
            return (2 ** 32 - solution) * -1

        return solution