class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # case 1: the subarray lies in the middle of the array:
        # use dp to find max_len_subarray
        max_subarray_sum = nums[0]
        arr = nums.copy()
        for index in range(1, len(nums)):
            if arr[index-1] > 0:
                arr[index] += arr[index-1]
            
            max_subarray_sum = max(max_subarray_sum, arr[index])
        
        if len(nums) < 3:
            return max_subarray_sum
        # case 2: the subarray is circluar meaning it has a hole in
        # the middle. So the Approach is to find the minimum subarray
        # that could lie inbetween (don't touch first and last element)
        # the array.
        total = sum(nums)
        min_subarray_sum = nums[1]
        # don't touch the first and last element b/c they're needed to make circular 
        for index in range(2, len(nums)-1):
            if nums[index-1] < 0:
                nums[index] += nums[index-1]
            
            min_subarray_sum = min(min_subarray_sum, nums[index])
        
        return max(
            max_subarray_sum,
            total - min_subarray_sum
        )
