class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n== 0:
            return False
        if n ==1:
            return True
        if n==3:
            return True
        elif n%3 == 0:
            return self.isPowerOfThree(n//3)
        return False
