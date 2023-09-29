class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        prefixSum = satisfaction.copy()

        for i in range(n-2, -1, -1):
            prefixSum[i] += prefixSum[i+1]
        prefixSum.append(0)

        totalSum = 0
        for index, num in enumerate(satisfaction):
            totalSum += (num*(index+1))
        
        res = totalSum
        for index, num in enumerate(satisfaction):
            totalSum -= (num + prefixSum[index+1])
            res = max(totalSum, res)
        
        return res
