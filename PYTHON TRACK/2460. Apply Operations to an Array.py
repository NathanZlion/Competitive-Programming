class Solution(object):
    def moveZeros(self, lst):
        if not lst:
            return []
        k = 0
        for i in range(len(lst)):
            if lst[i] != 0:
               lst[k] = lst[i]
               k+=1
        for j in range(k,len(lst)):
            lst[j] = 0

        return lst


    def applyOperations(self, nums):
        for index in range(len(nums) - 1):
            if nums[index] == nums[index +1]:
                nums[index] *= 2
                nums[index + 1] = 0

        return self.moveZeros(nums)
