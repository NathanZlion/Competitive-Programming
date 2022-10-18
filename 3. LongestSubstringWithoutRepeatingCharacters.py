class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []

        left = 0
        maxLength = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.append(s[right])

            currWindowSize = right - left +1
            maxLength = max(maxLength, currWindowSize)

        return maxLength
