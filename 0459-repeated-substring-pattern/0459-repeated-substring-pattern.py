class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        def canSegment(string: str, end: int) -> bool:
            n = len(string)

            if n % (end + 1) != 0:
                return False

            substring = string[:end+1]
            
            for start in range(end+1,n,end+1):
                if s[start:start+end+1] != substring:
                    return False

            return True
        
        
        for endIndex in range(len(s)//2):
            if canSegment(s, endIndex):
                return True

        return False