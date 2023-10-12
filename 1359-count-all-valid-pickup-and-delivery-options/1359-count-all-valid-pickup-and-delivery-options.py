class Solution:
    def countOrders(self, n: int) -> int:
        MOD = (10**9)+7

        return math.factorial(2 * n) // pow(2, n) % MOD
