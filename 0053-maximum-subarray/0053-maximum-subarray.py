class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_subarray_sum = nums[0]
        for index in range(1, len(nums)):
            if nums[index-1] > 0:
                nums[index] += nums[index-1]
            
            max_subarray_sum = max(max_subarray_sum, nums[index])

            
        return max_subarray_sum
