class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1.0:
            return True

        if int(n)!=n:
            return False
        
        return self.isPowerOfFour(n/4)