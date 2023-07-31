class Solution:
    def asciiValue(self, charCollection: str | list) -> int:
        return sum(ord(char) for char in charCollection)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        # added an extra layer of 0 as padding on the right and bottom

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                right = dp[row][col+1]
                bottom = dp[row+1][col]
                bottomright = dp[row+1][col+1]

                if s1[row]  == s2[col]:
                    bottomright += ord(s1[row])

                dp[row][col] = max(bottom, right, bottomright)

        s1AsciiValue = self.asciiValue(s1)
        s2AsciiValue = self.asciiValue(s2)

        return s1AsciiValue + s2AsciiValue - (2 * dp[0][0])
