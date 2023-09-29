class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        stones.sort()
        
        @cache
        def dp(index: int, runningSum: int) -> int:
            if index == len(stones)-1:
                return abs(runningSum)
            
            return min(
                dp(index+1, runningSum - stones[index]),
                dp(index+1, runningSum + stones[index])
            )
        
        return dp(-1, 0)