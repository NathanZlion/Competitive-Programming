class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(index):
            if index == n:
                return min(1, n)

            if s[index] == "0":
                return 0

            numOfWays = 0            
            numOfWays += dp(index+1)

            if index < n-1 and s[index:index+2] <= "26":
                numOfWays += dp(index+2)
            
            return numOfWays

        return dp(0)