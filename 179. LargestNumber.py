class Solution(object):
    def largestNumber(self, nums):

        def isLarger(x,y):
            return int(str(x) + str(y)) < int(str(y) + str(x))

        def bubbleSort(nums):
            for i in range(len(nums)-1):
                for j in range(i,len(nums)):
                    if isLarger(nums[i], nums[j]):
                        nums[i], nums[j] = nums[j], nums[i]

        bubbleSort(nums)
        strNum = []
        for num in nums:
            strNum.append(str(num))


        return str(int("".join(strNum)))
