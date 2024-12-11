class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        maxOutlier = -(inf)
        count = Counter(nums)
        
        for index in range(len(nums)):
            # let's try to exclude the current index
            numToExclude = nums[index]
            targetSum = totalSum - numToExclude
            
            # is the rest of the list sum to one of the nums
            # in the list
            if targetSum % 2:
                continue
            
            count[numToExclude] -= 1
            targetNum = targetSum // 2
            
            if count[targetNum] > 0:
                maxOutlier = max(maxOutlier, numToExclude)

            count[numToExclude] += 1
        
        return maxOutlier
