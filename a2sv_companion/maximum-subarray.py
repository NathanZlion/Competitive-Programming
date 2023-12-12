class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_prev = 0
        res = -inf
        running_sum = 0
        for num in nums:
            running_sum += num
            res = max(res, running_sum - min_prev)
            min_prev = min(min_prev, running_sum)

        return res
