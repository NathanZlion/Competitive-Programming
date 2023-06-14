class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        # trying the brute force approach
        if n == 1 or n == 0:
            return n
        
        nums = [0 for _ in range(n+1)]
        nums[0] = 0
        nums[1] = 1
        
        for index in range(2, n+1):
            nums[index] += nums[index//2]

            # odd indices
            if index % 2:
                nums[index] += nums[index//2 +1]
        
        return max(nums)
