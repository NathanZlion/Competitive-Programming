class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        
        if n in set([1,2]):
            return n
        
        curr_ways = self.memo[n] if n in self.memo else\
        self.climbStairs(n-1) + self.climbStairs(n-2)
        
        self.memo[n] = curr_ways

        return curr_ways
        


                
