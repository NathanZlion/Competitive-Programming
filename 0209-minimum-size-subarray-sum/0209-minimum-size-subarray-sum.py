class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = 1000000
        runningSum = 0
        left= 0
        n = len(nums)

        for right in range(n):
            runningSum += nums[right]

            while runningSum >= target:
                minLen = min(minLen, right-left+1)
                runningSum -= nums[left]
                left += 1

            if runningSum >= target:
                minLen = min(minLen, right-left+1)
        
        if minLen == 1000000:
            return 0

        return minLen                
        