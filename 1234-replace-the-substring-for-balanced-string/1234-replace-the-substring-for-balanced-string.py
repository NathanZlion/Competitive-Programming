class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        minimumLengthSubstring = n
        ctr = Counter(s)
        left = 0
        
        for right in range(n):
            ctr[s[right]] -= 1
            while left <= right:
                ctr[s[left]] += 1
                left += 1
                if not self.isBalanced(ctr, n//4):
                    left -= 1
                    ctr[s[left]] -= 1
                    break
            
            if self.isBalanced(ctr, n//4):
                minimumLengthSubstring = min(minimumLengthSubstring, right - left + 1)

        return minimumLengthSubstring


    def isBalanced(self, ctr, n):

        for k in ctr.keys():
            if ctr[k] > n:
                return False
        
        return True
        
    
        