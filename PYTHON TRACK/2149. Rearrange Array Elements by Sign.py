class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive_nums = []
        negative_nums = []

        for num in nums:
            if num > 0:
                positive_nums.append(num)
            else:
                negative_nums.append(num)
        
        half_length = len(positive_nums)
        arranged_arr = []
        for index in range(half_length):
            arranged_arr.append(positive_nums[index])
            arranged_arr.append(negative_nums[index])
        
        return arranged_arr
