class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        lastRow = len(triangle) - 1

        for col in range(lastRow + 1):
            memo[(lastRow, col)] = triangle[lastRow][col]
        
        def backTrack(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            min_child_sum = min(backTrack(row + 1, col), backTrack(row + 1, col + 1))
            memo[(row, col)] = min_child_sum + triangle[row][col]

            return memo[(row, col)]


        return backTrack(0,0)