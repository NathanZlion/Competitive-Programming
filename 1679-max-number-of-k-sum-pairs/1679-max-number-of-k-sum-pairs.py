class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        
        ptr1 = 0
        ptr2 = len(nums)-1
        
        maxOp = 0
        while ptr2 > ptr1:

            if nums[ptr1] + nums[ptr2] == k:
                maxOp += 1
                ptr1 += 1
                ptr2 -= 1

            elif nums[ptr1] + nums[ptr2] > k:
                ptr2 -= 1
            
            else:
                ptr1 += 1
        
        return maxOp
                
        
        