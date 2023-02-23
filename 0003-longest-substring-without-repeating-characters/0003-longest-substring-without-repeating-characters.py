class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        n = len(s)
        left = 0
        max_len = 0

        for right in range(n):
            while s[right] in uniques:
                uniques.remove(s[left])
                left += 1
                
            uniques.add(s[right])
            max_len = max(max_len, right-left+1)
        
        return max_len
            
                
                

                
        