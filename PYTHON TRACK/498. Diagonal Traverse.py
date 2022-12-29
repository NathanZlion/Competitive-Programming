class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        total_row = len(mat)
        total_col = len(mat[0])

        freq = {}

        for i in range(total_col + total_row):
            freq[i] = []

        # Both freq tables are now initialized, Now onto the traversal.
        for row in range(total_row -1, -1, -1):
            for col in range(total_col -1, -1, -1):
                freq[row + col].append(mat[row][col])

        res = []
        for i in range(total_col + total_row - 1):
            if i%2:  # odd diagonal sum
                res.extend(freq[i][::-1])
            else:
                res.extend(freq[i])

        return res
