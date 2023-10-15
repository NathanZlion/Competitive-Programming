class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
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