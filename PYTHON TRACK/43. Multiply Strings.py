class Solution(object):

    def toInt(self, num):
        res = 0

        while num:
            res = (res*10) + (ord(num[0]) -48)
            num = num[1:]

        return res

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(self.toInt(num1) * self.toInt(num2))
