class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ptr = len(digits) -1
        carry = 0

        while True:
            carry, digits[ptr] = (digits[ptr] + 1)//10, (digits[ptr] + 1)%10
            if (not carry):
                return digits
            elif (ptr > 0):
                ptr-=1
            else:
                digits = [carry]+digits
                return digits
