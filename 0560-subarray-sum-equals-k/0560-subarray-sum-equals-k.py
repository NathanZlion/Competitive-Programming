class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        count = 0
        
        prefixMap = defaultdict(int)
        prefixMap[0] = 1
        runningSum = 0

        for index in range(n):
            runningSum += nums[index]
            count += prefixMap[runningSum - k]
            prefixMap[runningSum] += 1

        return count
