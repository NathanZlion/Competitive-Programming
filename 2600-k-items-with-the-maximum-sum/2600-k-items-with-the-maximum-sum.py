class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        runningSum = 0
        
        # take the numOnes first
        if k > 0:
            runningSum += min(numOnes, k)
            k = k-numOnes if k >= numOnes else 0

        if k > 0:
            k -= numZeros
        
        if k > 0:
            runningSum -= min(k, numNegOnes)
        
        return runningSum
