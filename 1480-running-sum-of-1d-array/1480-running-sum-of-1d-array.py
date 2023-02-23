class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        return nums
        
