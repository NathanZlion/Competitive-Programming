class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        deadEnds = set()
        
        def isSame(word: str, startIndex: int) -> bool:
            for index in range(len(word)):
                if word[index] != s[startIndex + index]:
                    return False
            
            return True


        def canSegmentFromIndex(index: int) -> bool:
            if index in deadEnds:
                return False
            
            if index == len(s):
                return True
            
            # try fitting words at that index
            for word in wordDict:
                
                # word is too long to fit
                if len(word) > len(s) - index:
                    continue

                if isSame(word, index):
                    if canSegmentFromIndex(index + len(word)):
                        return True

            deadEnds.add(index)
            return False
        
        return canSegmentFromIndex(0)
