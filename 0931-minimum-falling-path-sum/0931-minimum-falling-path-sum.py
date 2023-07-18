from math import inf as infinity

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {(0, col): matrix[0][col] for col in range(n)}
        # directly up, diagonally left and diagonally right
        directions = [(-1, 0), (-1, -1), (-1, 1)]


        def climb_up(row, col) -> Optional[int]:
            if (row, col) in memo:
                return memo[(row, col)]
            
            # check if the row and col are inbound: if not return infinity
            if not (0 <= row < n and 0 <= col < n):
                return infinity

            min_prev_sum = infinity
            for r, c in directions:
                r += row
                c += col
                min_prev_sum = min(min_prev_sum, climb_up(r, c))

            memo[(row, col)] = min_prev_sum + matrix[row][col]
            return memo[(row, col)]

        min_path_sum = infinity
        for col in range(n):
            min_path_sum = min(min_path_sum, climb_up(n-1, col))
        
        return min_path_sum
