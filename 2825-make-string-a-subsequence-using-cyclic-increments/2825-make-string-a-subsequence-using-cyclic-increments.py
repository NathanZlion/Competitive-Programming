class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left_ptr = 0
        right_ptr = 0
        
        def nextCycle(char):
            res = chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))
            return res

        while left_ptr < len(str1) and right_ptr < len(str2):
            left = str1[left_ptr]
            right = str2[right_ptr]
            
            if left == right or (nextCycle(left) == right):
                right_ptr += 1
            
            left_ptr += 1
        
        return right_ptr == len(str2)
 