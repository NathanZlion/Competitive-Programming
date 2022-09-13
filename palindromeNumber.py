  def isPalindrome(self, x):
      if x < 0:
          return False
      num = str(x)
      # casted it to string :( 

      length = len(num)
      if length == 1:
          return True
      for i in range(length//2):
          if num[i] != num [length - i -1]:
              return False
      return True
