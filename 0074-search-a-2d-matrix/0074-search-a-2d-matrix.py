class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        number_of_rows = len(matrix)
        number_of_cols = len(matrix[0])

        def to_int(row: int, col: int) -> int:
            return number_of_cols * row + col

        def to_row_col(int_repr:int) -> Tuple[int, int]:
            return int_repr // number_of_cols, int_repr % number_of_cols
        
        start = -1
        end =  to_int(number_of_rows-1 , number_of_cols-1) + 1
        
        while start < end-1:
            mid = start + ((end-start)//2)
            mid_row, mid_col = to_row_col(mid)

            if matrix[mid_row][mid_col] > target:
                end = mid
            else:
                start = mid
        
        if start == -1:
            return False

        row, col = to_row_col(start)

        return matrix[row][col] == target