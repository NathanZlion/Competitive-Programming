from math import ceil, floor, sqrt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return ceil(sqrt(num)) == floor(sqrt(num))