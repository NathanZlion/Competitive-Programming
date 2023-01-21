class Solution(object):
    def sortColors(self, nums):
    
        oneStart = 0
        oneLength = 0
        for i in nums:
            if i == 0:
                oneStart += 1
            if i == 1:
                oneLength += 1
        
        twoStart = oneStart + oneLength
        for i in range(oneStart):
            nums[i] = 0
        for j in range(oneStart, twoStart):
            nums[j] = 1
        
        for k in range(twoStart,len(nums)):
            nums[k] = 2
                
