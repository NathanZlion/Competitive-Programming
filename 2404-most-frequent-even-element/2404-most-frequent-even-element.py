class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        count = defaultdict(int)
        for num in nums:
            if num%2 == 0:
                count[num] += 1
        
        maxFreqNum = inf
        maxFreq = -1
        for num in count:
            if num%2 == 0:
                if ( count[num] > maxFreq ) or ( count[num] == maxFreq and num < maxFreqNum ):
                    maxFreqNum = num
                    maxFreq = count[num]

        return maxFreqNum if maxFreqNum < inf else -1
