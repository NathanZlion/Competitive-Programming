class Solution(object):
    def sortArrayByParity(self, nums):
        newArr = [num for num in nums]
        p_even = 0
        p_odd = len(nums)-1

        for num in nums:
            # num is odd
            if num % 2:
                newArr[p_odd] = num
                p_odd -= 1
            # num is even
            else:
                newArr[p_even] = num
                p_even += 1
        
        return newArr