class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        longestSubstring = ""
        
        def isPalindrome(left, right):
            while right > left:
                if s[right]  != s[left]:
                    return False
                
                right -= 1
                left += 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(0, len(s) - length + 1):
                if isPalindrome(start, start + length - 1):
                    return s[start:start+length]

        return ""
