class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # whose length equals k max average
        runningSum = 0

        for index in range(k):
            runningSum += nums[index]

        maxSum = runningSum        
        for right in range(k, len(nums)):
            left = right - k
            runningSum += nums[right]
            runningSum -= nums[left]
            maxSum = max(maxSum, runningSum)
        
        return maxSum/k