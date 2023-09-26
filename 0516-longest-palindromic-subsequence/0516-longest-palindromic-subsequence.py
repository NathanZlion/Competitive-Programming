class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(left, right):
            if left == right:
                return 1
            
            if left == right - 1:
                return 2 if s[left] == s[right] else 1
            
            if s[left] == s[right]:
                return 2 + dp(left+1, right-1)

            return max(
                dp(left+1, right),
                dp(left, right-1)
            )
        
        return dp(0, n-1)
