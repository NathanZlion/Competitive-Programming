class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prev_sum = 0
        n = len(nums)
        total_sum = sum(nums)

        for index in range(n):
            if total_sum - prev_sum - nums[index] == prev_sum:
                return index
            
            prev_sum += nums[index]

        return -1
