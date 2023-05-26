class Solution:
    def __init__(self):
        self.memo = {
            -1: 0,
             0: 0,
             1: 1,
             2: 2,
        }

    def climbStairs(self, n: int) -> int:
        # previously computed n value
        if n in self.memo:
            return self.memo[n]
        
        # if n not previously computed, compute and save in memo
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)


        return self.memo[n]