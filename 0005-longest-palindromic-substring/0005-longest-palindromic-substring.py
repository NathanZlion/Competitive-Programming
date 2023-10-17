class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for right in range(n)] for left in range(n)]
        ans = [0, 0]

        # one letter is a palindrome for sure
        for i in range(n):
            dp[i][i] = True

        # for 2 letters to be palindrome we need them to be same
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                # guaranteed this has at least equal length with the prev and
                # cos we're iterating length in increasing order
                ans = [i, i + 1]

        # iterate throught different letter sizes
        for length in range(3, n+1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    ans = [left, right]


        left, right = ans
        return s[left: right + 1]