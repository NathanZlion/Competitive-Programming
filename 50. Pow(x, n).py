class Solution(object):
    def myPow(self, x, n):
        if n==0: return 1
        elif n==1: return x
        if n>1:
            if n%2==0: return pow(x, n//2)* pow(x, n//2)
            return pow(x, n//2) * pow(x, n//2 +1)
        else:
            return (x**n)
