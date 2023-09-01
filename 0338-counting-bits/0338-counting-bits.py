class Solution:
    @cache
    def numberOfBits(self, num : int) -> int:
        if num in self.memo:
            return self.memo[num]

        if num % 2:
            return self.numberOfBits(num>>1) + 1
        else:
            return self.numberOfBits(num>>1)

    def countBits(self, n: int) -> List[int]:
        self.memo = {0:0, 1:1}

        arr = [0 for _ in range(n+1)]

        for i in range(n+1):
            self.memo[i] = self.numberOfBits(i)
            arr[i] = self.memo[i]

        return arr