class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        self.total_sum = sum(nums)
        
        if self.total_sum % 2: #this means it's odd
            return False
        
        self.half_sum = self.total_sum // 2

        @cache
        def dp(index: int, runningSum: int) -> bool:
            if runningSum == self.half_sum:
                return True
            
            if index >= len(nums) or runningSum > self.half_sum:
                return False

            return dp(index+1, runningSum + nums[index]) or dp(index+1, runningSum ) 

        return dp(0, 0)