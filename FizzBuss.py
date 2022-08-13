def FizzBuzz(num):
  for i in range(num+1):
    buzzed = True
    if i%3==0:
      print('Fizz', end = "")
      buzzed = False
    if i%5==0:
      print('Buzz', end = "")
      buzzed = False
    if buzzed:
      print(i, end = "")
    print()
 
if __name__ == '__main__':
    try:
        num = int(input("Enter an integer: "))
        FizzBuzz(num)
    except ValueError:
        print("Invalid Input, Please Enter an Integer.")
