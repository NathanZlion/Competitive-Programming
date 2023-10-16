class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        count = 0
        
        prefixMap = {}
        prefixMap[0] = 1
        runningSum = 0

        for index in range(n):
            runningSum += nums[index]
            count += prefixMap.get(runningSum - k, 0)
            prefixMap[runningSum] = prefixMap.get(runningSum, 0) + 1

        return count
