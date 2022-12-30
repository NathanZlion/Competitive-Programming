class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        col_map = defaultdict(lambda: 0)
        row_map = defaultdict(lambda: 0)

        total_row = len(grid)
        total_col = len(grid[0])

        for row in range(total_row):
            for col in range(total_col):
                if grid[row][col]:         #if its a 1
                    row_map[row] += 1
                    col_map[col] += 1
                else:
                    row_map[row] -= 1
                    col_map[col] -= 1

        res = [[0 for _ in range(total_col)] for _ in range(total_row) ]


        for row in range(total_row):
            row_val = row_map[row]
            for col in range(total_col):
                col_val = col_map[col]
                res[row][col] = (col_val + row_val)


        return res

