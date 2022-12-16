class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i = j = pres = 0
        result = len(nums) + 1

        while j < len(nums):
            pres += nums[j]; j += 1
            while pres >= target:
                result = min(result, j - i)
                pres -= nums[i]; i+= 1

        if result != len(nums) + 1:
            return result
        return 0
