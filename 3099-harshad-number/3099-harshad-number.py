class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:        
        sumOfDigits = 0
        tempNum = x

        while tempNum:
            sumOfDigits += (tempNum % 10)
            tempNum //= 10
        
        if x % sumOfDigits > 0:
            return -1

        return sumOfDigits
