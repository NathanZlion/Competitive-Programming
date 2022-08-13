
class Solution(object):
    def fizzBuzz(self, n):
        msgout = []
        for i in range(1, n+1):
            msg = ""
            buzzed = True
            if i%3==0:
                msg += 'Fizz'
                buzzed = False
            if i%5==0:
                msg += 'Buzz'
                buzzed = False
            if buzzed:
                msg += str(i)
            msgout.append(msg)
            
        return msgout 
      
if __name__ == '__main__':
  try:
      num = int(input("Enter an integer: "))
      fizz = Solution()
      print(fizz.FizzBuzz(num))
  except ValueError:
      print("Invalid Input, Please Enter an Integer.")
      
