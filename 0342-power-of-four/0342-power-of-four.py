class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if int(n)!=n:
            return False

        if n == 0:
            return False

        if n == 1:
            return True
        
        return self.isPowerOfFour(n/4)