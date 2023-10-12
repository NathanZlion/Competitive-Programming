class Solution:
    def countOrders(self, n: int) -> int:
        MOD = (10**9)+7

        possibilities = 1
        for i in range(1, n+1):
            positions = (2*i) - 1
            possibilities *= (positions*(1+positions))//2
            possibilities %= MOD

        return possibilities
