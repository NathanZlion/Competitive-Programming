class Solution:
    def tribonacci(self, n: int) -> int:
        # i would have to keep track of the first
        # three numbers

        fib = [0] * (n+1)
        
        if n < 3:
            arr = {0: 0, 1: 1, 2: 1}
            return arr[n]
        
        fib[0] = 0
        fib[1] = 1
        fib[2] = 1
        
        for index in range(3, n+1):
            fib[index] = fib[index-1] + fib[index-2] + fib[index-3]
        
        return fib[n]
            
        
        