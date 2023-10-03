from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        numOfValidTriangles = 0
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                k = bisect_right(nums, nums[i]+nums[j]-1)
                numOfValidTriangles += max(k-j-1, 0)

        return numOfValidTriangles