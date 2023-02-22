class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        
        res = []
        newStr = sorted(s[:len(p)])
        p = sorted(p)
        
        if newStr == p:
            res.append(0)
        
        for end in range(len(p), len(s)):
            newStr.remove(s[end-len(p)])
            newStr.append(s[end])
            newStr.sort()
            if newStr == p:
                res.append(end-len(p)+1)
        
        return res
        
        
        
        
        
        