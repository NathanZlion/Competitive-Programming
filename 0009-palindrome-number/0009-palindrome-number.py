class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_num = 0
        num = x

        while num:
            reversed_num *= 10
            reversed_num += (num % 10)
            num //= 10

        return reversed_num == x