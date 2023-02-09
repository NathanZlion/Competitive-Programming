class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num1 = []
        num2 = []
        
        zNum = []
        
        n = len(str(num))
        ptr = 0
        for i in range(n):
            lstDigit = num % 10
            zNum.append(lstDigit)
            num //= 10
        
        zNum.sort()
        zNum = list(map(str, zNum))

        
        turn = True
        
        ptr = 0
        while ptr < n:
            if turn:
                num1.append(zNum[ptr])
            else:
                num2.append(zNum[ptr])
            
            turn = not turn
            ptr += 1
        
        num1 = "".join(num1)
        num2 = "".join(num2)

        return int(num1) + int(num2)

