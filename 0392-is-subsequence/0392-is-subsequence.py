class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0

        for index, char in enumerate(t):
            if ptr == len(s):
                return True
        
            if char == s[ptr]:
                ptr+=1
        
        return ptr == len(s)