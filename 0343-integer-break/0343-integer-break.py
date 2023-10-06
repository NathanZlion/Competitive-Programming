from math import pow

class Solution:
    def integerBreak(self, n: int) -> int:
        def maxProductForKParts(n: int, k: int) -> int:
            remainder = n%k
            product = int(pow((n // k+1), remainder))
            product *= int(pow((n // k), (k - remainder)))

            return product            

        maxProd = 1
        for k in range(2, n):
            maxProd = max(maxProd, maxProductForKParts(n, k))

        return maxProd
