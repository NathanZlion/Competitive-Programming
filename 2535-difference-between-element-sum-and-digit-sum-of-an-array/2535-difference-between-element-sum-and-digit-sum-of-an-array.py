class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digitSum(num):
            sum_ = 0 
            while num:
                sum_ += (num % 10)
                num //= 10
            
            return sum_

        elemSum = 0
        digSum = 0
        
        for num in nums:
            elemSum += num
            digSum += digitSum(num)
        
        return abs(elemSum - digSum)
        