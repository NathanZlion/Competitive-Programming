class Solution(object):
    def countDistinctIntegers(self, nums):

        def reverse(num):
            res = 0
            while num:
                res*=10
                res += num%10
                num //= 10

            return res

        uniques = set()
        for num in nums:
            uniques.add(num)
            uniques.add(reverse(num))
        
        return len(uniques)
