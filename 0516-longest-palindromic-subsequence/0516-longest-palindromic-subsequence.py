class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        n = len(s)

        def palindromeLength(left = 0, right = n-1):
            # base cases
            if (left, right) in memo:
                return memo[(left, right)]

            if right == left:
                return 1

            if right - left == 1:
                return 2 if s[left] == s[right] else 1

            if s[left] == s[right]:
                memo[(left, right)] = 2 + palindromeLength(left+1, right-1)
                return 2 + palindromeLength(left+1, right-1)
            else:
                memo[(left, right)] = max(palindromeLength(left+1, right),palindromeLength(left, right-1))

            return memo[(left, right)]


        return palindromeLength()