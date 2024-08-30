class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        values = [freq[key] for key in sorted(freq.keys())]
        keys = sorted(freq.keys())

        n = len(values)
        if n < 2:
            return 0
        
        runningSum = freq[keys[0]] + freq[keys[1]]
        maxSum = runningSum if keys[1] - keys[0] == 1 else 0

        for right in range(2, n):
            runningSum += freq[keys[right]]
            runningSum -= freq[keys[right - 2]]
            if keys[right] - keys[right-1] == 1:
                maxSum = max(maxSum, runningSum)

        return maxSum
