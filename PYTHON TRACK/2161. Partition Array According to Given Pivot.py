class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lessThan = []
        greaterThan = []
        equalTo = []
        for num in nums:
            if num > pivot:
                greaterThan.append(num)
            elif num < pivot:
                lessThan.append(num)
            else:
                equalTo.append(num)
        
        nums = lessThan + equalTo + greaterThan
        return nums
