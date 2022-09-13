  def isPalindrome(num):
      if num < 0:
          return False
      strNum = str(num)
      # casted it to string :( 

      length = len(strNnum)
      if length == 1:
          return True
      for i in range(length//2):
          if strNum[i] != strNum [length - i -1]:
              return False
      return True
