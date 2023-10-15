class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        this problem looks like a dp problem.
        it has two states that have to be tracked:
        :: index
        :: num of steps remaining
        
        to better understand the problem let's build a top down approach for this
        This is a working solution yet it needs to be optimized inorder to avoid a TLE
        """

        modulo = 10**9 + 7
        
        def isInbound(index: int) -> bool:
            return 0 <= index < arrLen

        @cache
        def dp(index: int, stepsRemaining: int) -> None:

            if stepsRemaining == 0:
                if index == 0:
                    return 1
                
                return 0
        
            if not isInbound(index):
                return 0

            stepsRemaining -= 1
            return (
                dp(index, stepsRemaining) +
                dp(index-1, stepsRemaining) +
                dp(index+1, stepsRemaining)
            ) % modulo


        return dp(0, steps)