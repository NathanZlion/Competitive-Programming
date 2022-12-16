class Solution(object):
    def isPalindrome(self, s):
        
        s=s.lower()
        
        ptr_1 = 0
        ptr_2 = len(s)-1
        
        while ptr_1 <= ptr_2:
            if (not (s[ptr_1].isalpha() or s[ptr_1].isalnum())):
                ptr_1 += 1
            elif (not (s[ptr_2].isalpha() or s[ptr_2].isalnum())):
                ptr_2 -= 1
            else:
                if (s[ptr_1] == s[ptr_2]):
                    ptr_1 += 1
                    ptr_2 -= 1
                    continue
                return False
        return True
