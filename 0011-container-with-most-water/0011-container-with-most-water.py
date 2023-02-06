class Solution:
    def maxArea(self, height):
        maxarea, i, j = 0, 0, len(height)-1

        while (i < j):
            res = min(height[i], height[j]) * (j-i)
            maxarea=max(maxarea,res)

            if height[i] <= height[j]:
                i += 1

            else:
                j -= 1

        return maxarea
