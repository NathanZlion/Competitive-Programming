class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[r, c] for r in range(rows) for c in range(cols)], key = lambda pos: abs(pos[0] - rCenter) + abs(pos[1] - cCenter))