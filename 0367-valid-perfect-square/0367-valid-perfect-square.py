from math import ceil, floor, sqrt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(sqrt(num)) == sqrt(num)
