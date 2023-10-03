class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        numOfValidTriangles = 0
        n = len(nums)
        for k in range(n-1, 1, -1):
            i = 0
            for j in range(k-1, 0, -1):
                if i >= j:
                    break

                while j > i and nums[i]+nums[j] <= nums[k]:
                    i += 1

                if nums[i]+nums[j] > nums[k]:
                    numOfValidTriangles += (j-i)
        
        return numOfValidTriangles