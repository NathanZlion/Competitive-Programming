class Solution(object):
    def isImaginary(self, num):
        try:
            int(num)
            return False
        except:
            return True

    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        real_part = 0
        imaginary_part = 0

        num1_splitted = num1.split("+")
        num2_splitted = num2.split("+")

        for num1 in num1_splitted:
            for num2 in num2_splitted:

                if self.isImaginary(num1) and self.isImaginary(num2):
                    real_part -= int(num1[:len(num1)-1]) * int(num2[:len(num2)-1])

                elif self.isImaginary(num1):
                    imaginary_part += int(num1[:len(num1)-1]) * int(num2)

                elif self.isImaginary(num2):
                    imaginary_part += int(num2[:len(num2)-1]) * int(num1)

                else:
                    real_part += int(num1) * int(num2)

        if imaginary_part>=0:
            product = str(real_part) + "+" + str(imaginary_part) + "i"

        else:
            product = str(real_part) + "+" + str(imaginary_part) + "i"


        return product

