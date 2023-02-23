class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = [0 for _ in range(26)]
        for char in s1:
            s1Counter[ord(char)-97] += 1
            
        subCounter = [0 for _ in range(26)]
        n = len(s1)
        m =  len(s2)
        left = 0
        for right in range(m):
            subCounter[ord(s2[right])-97] += 1
            
            while right-left+1 > n:
                subCounter[ord(s2[left])-97] -= 1
                left += 1

            if right-left+1 == n and subCounter == s1Counter:
                return True                
            
        
        return False