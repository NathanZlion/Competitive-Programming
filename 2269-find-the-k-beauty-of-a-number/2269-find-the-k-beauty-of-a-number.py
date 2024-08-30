class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numDigits = ceil(log(num + 1, 10))
        kBeauty = 0
        print(numDigits)

        for i in range(numDigits - k + 1):
            DIVISOR = 10 ** i
            MODULO = 10 ** k
            currNum = (num // DIVISOR) % MODULO

            if currNum == 0:
                continue

            if num % currNum == 0:
                kBeauty += 1
        
        return kBeauty
