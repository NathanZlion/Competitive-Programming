class Solution:
    def findComplement(self, num: int) -> int:
        binaries = []

        while num:
            binaries.append(num%2)
            num //= 2

        res = 0
        for i in range(len(binaries)-1, -1, -1):
            res<<=1
            res += 0 if binaries[i] else 1


        return res