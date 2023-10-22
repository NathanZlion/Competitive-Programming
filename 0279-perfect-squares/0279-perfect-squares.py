class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf for _ in range(n+1)]
        perfect_squares = [i*i for i in range(1, ceil(sqrt(n+1)))]

        for i in range(1, ceil(sqrt(n+1))):
            dp[i*i] = 1

        for num in range(n+1):
            for perf_num in perfect_squares:
                if perf_num >= num:
                    break

                dp[num] = min(dp[num], dp[num - perf_num] + 1)

        return dp[n]