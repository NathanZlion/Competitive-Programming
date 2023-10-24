class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix_product = [1 for _ in range(n+1)]
        for index in range(1, n+1):
            prefix_product[index] = prefix_product[index-1] * nums[index-1]

        suffix_product = [1 for _ in range(n+1)]
        for index in range(n-1, -1, -1):
            suffix_product[index] = suffix_product[index+1] * nums[index]
        
        return [prefix_product[index] * suffix_product[index+1] for index in range(n)]