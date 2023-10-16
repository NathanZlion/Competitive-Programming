class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = runningSum = 0
        prefixMap = {0: 1}

        for index in range(N):
            runningSum += nums[index]
            count += prefixMap.get(runningSum - k, 0)
            prefixMap[runningSum] = prefixMap.get(runningSum, 0) + 1

        return count
