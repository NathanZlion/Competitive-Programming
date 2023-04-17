class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        ptr1 = len(a) - 1
        ptr2 = len(b) - 1

        while ptr1 >= 0 or ptr2 >= 0 or carry > 0:

            if ptr1 >= 0:
                carry += int(a[ptr1])
                ptr1 -= 1

            if ptr2 >= 0:
                carry += int(b[ptr2])
                ptr2 -= 1

            res.append(str(carry % 2))
            carry //= 2

            
        return ''.join(res[::-1])
