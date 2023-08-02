class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [0]*n
        suffix_prod = [0]*n
        
        prefix_prod[0] = nums[0]
        suffix_prod[n-1] = nums[n-1]
        
        for index in range(1, n):
            prefix_prod[index] = prefix_prod[index-1] * nums[index]
        
        for index in range(n-2, 0, -1):
            suffix_prod[index] = suffix_prod[index+1] * nums[index]
        
        res = [0]*n
        res[0] = suffix_prod[1]
        res[n-1] = prefix_prod[n-2]

        for index in range(1, n-1):
            res[index] = prefix_prod[index-1] * suffix_prod[index+1]
        
        return res