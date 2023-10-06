from math import prod

class Solution:
    def integerBreak(self, n: int) -> int:
        def divideIntoKParts(num: int, k: int) -> List[int]:
            minVal = num//k
            arr = [minVal for _ in range(k)]

            remainder = num%k
            for i in range(remainder):
                arr[i] += 1
            
            return arr

        maxProd = 1
        for k in range(2, n):
            partitions = divideIntoKParts(n, k)
            maxProd = max(maxProd, prod(partitions))
        
        return maxProd
