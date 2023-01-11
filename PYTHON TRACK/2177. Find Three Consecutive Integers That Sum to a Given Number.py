class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3:
            # num is not divisible by 3
            return []
        mid = num //3
        return [mid-1, mid, mid+1]
