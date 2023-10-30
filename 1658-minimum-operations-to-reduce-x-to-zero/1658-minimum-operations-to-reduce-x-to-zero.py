class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        targetWindowSum = totalSum - x

        left = 0
        runningSum = 0
        maxWindowSize = -1

        for right in range(n):
            runningSum += nums[right]
            while runningSum > targetWindowSum and right >= left:
                runningSum -= nums[left]
                left += 1

            if runningSum == targetWindowSum:
                windowSize = right - left + 1
                maxWindowSize = max(maxWindowSize, windowSize)

        return n - maxWindowSize if maxWindowSize != -1 else -1
