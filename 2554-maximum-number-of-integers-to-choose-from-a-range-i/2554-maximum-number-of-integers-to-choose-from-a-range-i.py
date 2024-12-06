class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        runningSum = 0
        count = 0

        for num in range(1, n + 1):
            if num not in banned:
                if runningSum + num > maxSum:
                    break

                runningSum += num
                count += 1

        return count
