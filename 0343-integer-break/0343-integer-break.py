from math import pow

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def maxProductForKParts(n: int, k: int) -> int:
            remainder = n%k
            product = int(pow((n // k+1), remainder))
            product *= int(pow((n // k), (k - remainder)))

            return product            

        left = 2
        right = n+1
        while right > left + 1:
            mid = (right + left)//2
            if maxProductForKParts(n, mid) > maxProductForKParts(n, mid-1):
                left = mid
            else:
                right = mid


        return maxProductForKParts(n, left)
