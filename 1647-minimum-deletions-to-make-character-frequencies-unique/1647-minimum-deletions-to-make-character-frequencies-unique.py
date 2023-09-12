class Solution:
    def minDeletions(self, s: str) -> int:        
        charFreq = Counter(s)
        maxFreq = 0
        freqGroup = defaultdict(int)
        
        for char, freq in charFreq.items():
            freqGroup[freq] += 1
            maxFreq = max(maxFreq, freq)
        
        res = 0

        for freq in range(maxFreq, 0, -1):
            numSameFreq = freqGroup[freq]
            if numSameFreq > 1:
                res += (numSameFreq-1)
                freqGroup[freq-1] += (numSameFreq-1)
        
        return res