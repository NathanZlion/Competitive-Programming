class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        def isInbound(row: int, col: int) -> bool:
            return 0 <= row < n and 0 <= col < n

        def overlapCount(img1: int, img2: int, translationr: int, translationc: int) -> int:
            overlapCount = 0

            for row in range(n):
                for col in range(n):
                    if isInbound(row + translationr, col + translationc):
                        overlapCount += (img1[row][col] & img2[translationr + row][translationc + col])

            return overlapCount

        maxOverlap = 0
        for translationr in range(-n+1, n):
            for translationc in range(-n+1, n):
                maxOverlap = max(maxOverlap, overlapCount(img1, img2, translationr, translationc))

        return maxOverlap
