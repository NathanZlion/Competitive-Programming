class Solution:
    def minimumOneBitOperations(self, num: int) -> int:
        if num == 0:
            return 0

        k = 0
        curr = 1
        while (curr * 2) <= num:
            curr *= 2
            k += 1

        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(num ^ curr)
