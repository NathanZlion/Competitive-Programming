class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainderCount = defaultdict(int)
        for num in arr:
            remainderCount[num % k] += 1

        for remainder in remainderCount:
            complimentRemainder = (k - remainder) % k

            if remainder == complimentRemainder and remainderCount[remainder] % 2 != 0:
                return False

            if remainderCount[remainder] != remainderCount[complimentRemainder]:
                return False

        return True
