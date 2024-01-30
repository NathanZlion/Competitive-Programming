class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        A brute force approach that I could think of is to
        do a triple for loop,
        
        But this would have a time complexity of (n^3)
        nlog(n) + n^3
        
        We would have to come up with a better algorithm,
        First sort them.
        [ -4 -1 -1  0  1  2 ]
           l  r  ^
        """
        n = len(nums)
        nums.sort()
        visited = set()

        res = []
        for i in range(2, n):
            left = 0
            right = i - 1
            while right > left:
                # check if the sum of the 3 is greater than 0
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    if (nums[left], nums[right], nums[i]) not in visited:
                        res.append([nums[left], nums[right], nums[i]])
                        visited.add((nums[left], nums[right], nums[i]))

                    left += 1

        return res