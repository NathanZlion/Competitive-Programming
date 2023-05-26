class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n

        curr_fib =  self.memo[n] if n in self.memo else self.fib(n-1) + self.fib(n-2)
        self.memo[n] = curr_fib

        return curr_fib
        
            
        