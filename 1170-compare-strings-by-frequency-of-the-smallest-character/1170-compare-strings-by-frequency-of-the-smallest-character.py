class Solution:
    def freq_smallest_char(self, word):
        freq = defaultdict(int)

        for c in word:
            freq[c] += 1

        smallest_char = min(freq.keys())

        return freq[smallest_char]

    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freqOfSmallersChar = [self.freq_smallest_char(word) for word in words]
        freqOfSmallersChar.sort()
        totalWords = len(words)
        
        
        res = []
        for query in queries:
            queryFreq = self.freq_smallest_char(query)
            low = -1
            high = totalWords

            while high > low+1:
                mid = low + (high-low)//2

                if freqOfSmallersChar[mid] > queryFreq:
                    high = mid
                else:
                    low = mid
                    
            res.append(totalWords-low-1)
        
        return res
        