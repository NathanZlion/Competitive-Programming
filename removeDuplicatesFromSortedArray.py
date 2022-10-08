class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique=0
        pointer = 1
        while pointer<len(nums):
            if nums[unique] == nums[pointer]:
                pass
            else:
                unique +=1
                nums[unique], nums[pointer] = nums[pointer], nums[unique]
            pointer += 1
        return unique +1
        

