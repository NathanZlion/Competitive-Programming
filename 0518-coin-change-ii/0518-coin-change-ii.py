class Solution:
    def change(self, target_amount: int, coin_denominations: List[int]) -> int:
        num_coins = len(coin_denominations)

        dp = [[0] * (target_amount + 1) for _ in range(num_coins + 1)]

        for i in range(num_coins + 1):
            dp[i][0] = 1

        for coin_index in range(num_coins - 1, -1, -1):
            for current_amount in range(1, target_amount + 1):
                dp[coin_index][current_amount] = dp[coin_index + 1][current_amount]

                if coin_denominations[coin_index] <= current_amount:
                    dp[coin_index][current_amount] += (dp[coin_index][current_amount - coin_denominations[coin_index]])
        

        return dp[0][target_amount]
