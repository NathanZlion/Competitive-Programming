class Solution:        
    def rob(self, nums: List[int]) -> int:
        self.nums = nums

        return max(self.dp(0), self.dp(1))
    
    @lru_cache
    def dp(self, index):
        if index > len(self.nums)-1:
            return 0

        # try moving back 2 steps back and 3 steps back
        return max(self.dp(index+2), self.dp(index+3)) + self.nums[index]
