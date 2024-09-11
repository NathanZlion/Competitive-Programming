class Solution:
    def getFreqOfChars(self, word: str) -> Optional[Dict[str, int]]:
        res = {}
        for char in word:
            if char == " " or char.isnumeric():
                continue
            
            res[char.lower()] = res.get(char.lower(), 0) + 1
        
        return res

    def isCompleting(self, wordFreq: Dict[str, int], licensePlateFreq: Dict[str, int]) -> bool:
        for key, val in licensePlateFreq.items():
            if wordFreq.get(key, 0) < val:
                return False

        return True
        

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlateFreq = self.getFreqOfChars(licensePlate)
        shortestCompletingWord = None
        
        for word in words:
            wordFreq = self.getFreqOfChars(word)

            if self.isCompleting(wordFreq, licensePlateFreq) \
                and (shortestCompletingWord is None or len(word) < len(shortestCompletingWord)):
                shortestCompletingWord = word

        return shortestCompletingWord
