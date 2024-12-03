class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        quot = (dividend / divisor)
        if quot > 0:
            quot = math.floor(quot)
        else:
            quot = math.ceil(quot)

        if quot > (2**31  - 1):
            return 2**31

        elif quot < (-2**31):
            return -2**31

        return quot