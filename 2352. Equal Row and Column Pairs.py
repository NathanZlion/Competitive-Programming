class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        tot_rows = len(grid)
        tot_cols = len(grid[0])
        for row_idx in range(tot_rows):
            for col_idx in range(tot_cols):
                rows[row_idx].append(grid[row_idx][col_idx])
                cols[col_idx].append(grid[row_idx][col_idx])
        
        counter = 0
        for row in rows:
            for col in cols:
                if rows[row] == cols[col]:
                    counter += 1
        
        return counter
