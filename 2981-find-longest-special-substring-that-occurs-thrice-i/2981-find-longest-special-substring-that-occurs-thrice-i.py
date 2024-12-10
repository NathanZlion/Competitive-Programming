import string

class Solution:
    def numOccurrence(self, s: str, letter: str, substringLength: int) -> int:
        left = -1
        count = 0
        charCount = 0
        
        for right in range(len(s)):
            if s[right] == letter:
                charCount += 1
            
            # window is greater than character count
            # meaning there are other characters
            while charCount < (right - left):
                # print(left, substringLength, letter)
                if s[left + 1] == letter:
                    charCount -= 1

                left += 1

            # print(left, right, substringLength, letter)
            if charCount == substringLength:
                count += 1
                left += 1
                charCount -= 1

        # print(count)
        return count
    
    def maximumLength(self, s: str) -> int:
        strLength = len(s)
        res = 0
        
        # bruteforce
        for letter in string.ascii_lowercase:
            # number of occurrence
            for length in range(1, strLength - 1):
                count = self.numOccurrence(s, letter, length)
                if count >= 3:
                    # print(count, letter)
                    res = max(res, length)
        
        return res or -1
