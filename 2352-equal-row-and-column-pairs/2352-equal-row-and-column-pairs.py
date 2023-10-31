class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_count = defaultdict(int)
        row_count = defaultdict(int)

        for col in range(n):
            col_arr = []
            for row in range(n):
                col_arr.append(grid[row][col])

            col_count[hash(tuple(col_arr))] += 1

        for row in range(n):
            row_count[hash(tuple(grid[row]))] += 1

        res = 0
        for row_hash in row_count:
            res += (row_count[row_hash] * col_count[row_hash])

        return res
