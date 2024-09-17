class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1Count = Counter(s1.split(" "))
        words2Count = Counter(s2.split(" "))
        
        res = []
        for word in s1.split(" "):
            if words1Count[word] == 1 and words2Count[word] == 0:
                res.append(word)
            
        for word in s2.split(" "):
            if words2Count[word] == 1 and words1Count[word] == 0:
                res.append(word)
        
        return res
