class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math

        productArray = []
        currProduct = math.prod(nums[1:])
        productArray.append(currProduct)
        currIndex = 0

        while currIndex < len(nums)-1:
            currProduct *= nums[currIndex]
            currIndex += 1
            if nums[currIndex] != 0 :
                currProduct //= nums[currIndex]
                productArray.append(currProduct)
            else:
                productArray.append(math.prod(nums[:currIndex]) * math.prod(nums[currIndex+1:]))

        return productArray
