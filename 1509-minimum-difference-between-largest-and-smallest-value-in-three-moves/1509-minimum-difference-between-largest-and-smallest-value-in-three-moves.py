class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) < 5:
            return 0

        nums.sort()
        
        def backtrack(left, right, moves = 0):
            if moves == 3:
                return nums[right] - nums[left]
            
            return min(backtrack(left+1, right, moves+1), \
                       backtrack(left, right-1, moves+1) )

        return backtrack(left = 0, right = len(nums)-1)
