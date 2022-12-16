class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        import math
        pivotIndex  = 0
        leftSum = 0
        rightSum = math.fsum(nums[1:])

        while pivotIndex < len(nums)-1:
            if leftSum == rightSum:
                return pivotIndex
            else:
                leftSum += nums[pivotIndex]
                pivotIndex += 1
                rightSum -= nums[pivotIndex]
        
        if leftSum == 0:
            return pivotIndex
        return -1
