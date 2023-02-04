class Solution(object):
    def isHappy(self, n):        
        if n == 1:
            return True
        
        numbers = set()
        
        while True:
            if len(str(n)) == 1:
                n = n**2

            else:
                num = 0
                n = str(n)
                
                for i in range(len(n)):
                    num += pow(int(n[i]),2)
                    # n = (int(str(n)[0]))**2 + (int(str(n)[1]))**2
                n = num
                    
            if n not in numbers:
                numbers.add(n)
            else:
                return False

            if n == 1:
                return True
        
        return False            
