class Solution(object):
    def rotate(self, nums, k):

        n = len(nums)
        newArr = [num for num in nums]

        for i in range(n):
            nums[i] = newArr[(i-k)%n]
