class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @cache
        def palindromeLength(left, right):
            if right == left:
                return 1

            elif right == left + 1:
                return 2 if s[left] == s[right] else 1

            elif s[left] == s[right]:
                return 2 + palindromeLength(left+1, right-1)

            return max (
                palindromeLength(left+1, right),
                palindromeLength(left, right-1)
            )

        return palindromeLength(left = 0, right= len(s)-1)