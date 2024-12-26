class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        memo = {
            (length, 0): 1,
        }

        def dp(currIndex: int, targetSum: int) -> int:
            if (currIndex, targetSum) in memo:
                return memo[(currIndex, targetSum)]
            
            if currIndex == length:
                return 0

            numWays = 0
            # use positive
            numWays += dp(currIndex + 1, targetSum + nums[currIndex])
            
            # use negative
            numWays += dp(currIndex + 1, targetSum - nums[currIndex])
            
            memo[(currIndex, targetSum)] = numWays
            return numWays
        
        dp(0, target)
        return memo[(0, target)]
        