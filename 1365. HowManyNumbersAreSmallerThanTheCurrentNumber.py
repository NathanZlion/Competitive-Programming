class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        counter = [0 for i in range(500)]
        
        for num in nums:
            counter[num] += 1
        
        nums_lessthan = [0 for i in range(500)]

        sum_ = 0
        for num, occurance in enumerate(counter):
            nums_lessthan[num] = sum_
            sum_ += occurance

        for i in range(len(nums)):
            nums[i] = nums_lessthan[nums[i]]
        
        return nums
