class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort()
        n = len(piles)
        for i in range(n//3, n, 2):
            res += piles[i]

        return res
