class Solution(object):
    def isPalindrome(self, x):

        if (x < 0):
            return False

        temp = x
        newNum = 0
        
        while (x):
            newNum = (newNum*10) + (x %10)
            x //= 10

        return (newNum == temp)
