class Solution(object):
    def sortArrayByParity(self, nums):
        evens = []
        odds = []
        for num in nums:
            if num % 2:
                odds.append(num)
            else:
                evens.append(num)
        
        evens.extend(odds)
        return evens
        