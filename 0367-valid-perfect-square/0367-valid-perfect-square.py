from math import log, ceil, floor, sqrt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return ceil(sqrt(num)) == floor(sqrt(num))