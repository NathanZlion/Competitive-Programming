class Solution:
    def isPalindrome(self, s: str) -> bool:
        validCharacters = []
        for char in s:
            if char.isalpha():
                validCharacters.append(char.lower())
            elif char.isdigit():
                validCharacters.append(char)
        n = len(validCharacters)
        for left in range(n//2):
            right = n - left -1
            if validCharacters[left] != validCharacters[right]:
                return False
        return True