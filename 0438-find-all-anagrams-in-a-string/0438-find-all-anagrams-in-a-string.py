class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        countp = [0 for _ in range(26)]
        for char in p:
            countp[ord(char)-97] += 1
        
        k = len(p)
        counts = [0 for _ in range(26)]
        
        n = len(p)
        m = len(s)
        
        res = []
        left = 0
        for right in range(m):
            counts[ord(s[right])-97] += 1
            if right-left+1 == n:
                if counts == countp:
                    res.append(left)
                counts[ord(s[left])-97] -= 1
                left += 1
            

        return res
