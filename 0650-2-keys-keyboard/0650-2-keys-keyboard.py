from math import inf

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        @cache
        def dp(curr, clipboard):
            if curr == n:
                return 0

            if curr > n:
                return inf

            return min(
                dp(curr=curr*2, clipboard=curr) + 2,
                dp(curr=curr+clipboard, clipboard=clipboard) + 1
            )

        return dp(1, 1) + 1