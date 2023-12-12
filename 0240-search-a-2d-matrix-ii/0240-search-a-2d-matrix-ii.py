class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        I am thinking of doing a binary search on every row in the array
        
        time: 0(row * log (col))
        """
        col_len = len(matrix[0])
        
        for row in matrix:
            # do a binary search
            left = -1
            right = col_len
            
            while right > left + 1:
                mid = (left + right) // 2
                if row[mid] > target:
                    right = mid
                else:
                    left = mid
            if row[left] == target:
                return True
        
        return False
