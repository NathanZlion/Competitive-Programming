class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m + n - 2) / (factorial(n - 1) * factorial(m - 1)))