class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
#         0(nlogn + n) => 0(nlogn)

        for index in range(len(nums)):
            if index != nums[index]:
                return index
        
        return len(nums)
