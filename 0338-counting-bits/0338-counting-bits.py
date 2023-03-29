class Solution:
    def numberOfBits(self, num : int) -> int:
        bitCount = 0
        while num:
            bitCount += num%2
            num >>= 1

        return bitCount

    def countBits(self, n: int) -> List[int]:
        arr = [0 for _ in range(n+1)]

        for i in range(n+1):
            arr[i] = self.numberOfBits(i)

        return arr
