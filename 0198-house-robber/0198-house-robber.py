class Solution:
    
    def __init__(self):
        self.memo = {
            -1: 0,
            -2: 0,
            -3: 0,
        }
        
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        
        return max(self.dp(len(nums) - 1), self.dp(len(nums) - 2))

    def dp(self, index):
        # if already in memo return that
        if index in self.memo:
            return self.memo[index]
        
        # try moving back 2 steps back and 3 steps back
        max_possibility = max(self.dp(index-2), self.dp(index-3))
        max_possibility += self.nums[index]
        self.memo[index] = max_possibility
        return max_possibility
        
        
        