class Solution:
    def maxArea(self, H: List[int]) -> int:

        maxarea, i, j = 0, 0, len(H)-1
        while (i < j):
            res = min(H[i], H[j]) * (j-i)
            if res > maxarea: maxarea = res

            if H[i] <= H[j]:
                i += 1
            else:
                j -= 1

        return maxarea
