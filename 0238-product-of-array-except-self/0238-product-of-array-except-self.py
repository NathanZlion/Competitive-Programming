class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefixProd = [1]
        suffixProd = nums
        for num in nums:
            prefixProd.append((prefixProd[-1] * num))
        
        for j in range(n-2,-1,-1):
            suffixProd[j] *= suffixProd[j+1]
        suffixProd.append(1)


        ans = []
        
        for index in range(n):
            ans.append(prefixProd[index] * suffixProd[index+1])


        return ans
