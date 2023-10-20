class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLength = len(nums) + 1
        left = 0
        runningSum = 0

        for right in range(len(nums)):
            runningSum += nums[right]
            
            # minimize window size
            while runningSum >= target:
                minLength = min(minLength, right - left + 1)
                runningSum -= nums[left]
                left += 1

        if minLength <= len(nums):
            return minLength

        return 0
