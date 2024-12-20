class Solution:
    def productOfDigits(self, num: int) -> int:
        prod = 1
        for digit in str(num):
            prod *= int(digit)
        
        return prod
            
    def smallestNumber(self, n: int, t: int) -> int:
        currNum = n
        while True:
            if self.productOfDigits(currNum) % t == 0:
                return currNum
            
            currNum += 1
        