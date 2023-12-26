class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        modulus = 10**9 + 7
        
        @cache
        def dp(numDice, targetSum) -> int:
            if targetSum < 1:
                return 0

            if numDice == 0:
                return int(targetSum == 0)
            
            if numDice == 1:
                return int(1 <= targetSum <= k)

            allPoss =  0
            for i in range(1, k + 1):
                allPoss += dp(numDice-1, targetSum - i)
                allPoss %= modulus
            
            return allPoss % modulus
    
        return dp(n, target)
