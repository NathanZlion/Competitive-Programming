class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        compMap = dict()
        for i, num in enumerate(nums):
            comp = target - num
            if num in compMap:
                return [compMap[num],i]
            compMap[comp] = i
