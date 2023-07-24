from math import inf as infinity

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [infinity]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for index in range(coin, amount+1):
                dp[index] = min(dp[index], 1+dp[index - coin])

        return dp[amount] if dp[amount] < inf else -1
