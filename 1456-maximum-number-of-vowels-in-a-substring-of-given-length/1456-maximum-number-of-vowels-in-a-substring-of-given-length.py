class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # fixed window sliding problem 
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        runningVowelCount = 0
        for idx in range(k):
            if s[idx] in vowels:
                runningVowelCount += 1
        
        maxVowelCount = runningVowelCount
        
        for right in range(k, len(s)):
            left = right - k
            if s[left] in vowels:
                runningVowelCount -= 1
            
            if s[right] in vowels:
                runningVowelCount += 1
            
            
            maxVowelCount = max(maxVowelCount, runningVowelCount)
        
        return maxVowelCount