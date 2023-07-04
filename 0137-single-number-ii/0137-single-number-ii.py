class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        mask = 1
        limit = 2**32
        solution = 0
        
        while mask < limit:
            onesCount = 0
            
            for num in nums:
                onesCount += (num & mask)

            # count is not a multiple of 3
            # meaning it is on in the unique number
            if (onesCount % 3):
                solution |= mask # flip on that bit

            mask <<= 1
        
        # if sign bit is on (is negative)
        if solution & (1 << 31) != 0:
            negativeSolution = -(2 ** 32 - solution)
            return negativeSolution

        return solution