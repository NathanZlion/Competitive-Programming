class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def representative(coord):
            while coord != reps[coord]:
                coord = reps[coord]

            return coord

        def union(coord1, coord2):
            rep1 = representative(coord1)
            rep2 = representative(coord2)

            reps[rep1] = rep2

        reps = {(a,b): (a,b) for a,b in stones}
        lastRowCol = {}
        lastColRow = {}

        for r,c in stones:
            if r in lastRowCol:
                col = lastRowCol[r]
                union((r,c), (r, col))

            if c in lastColRow:
                row = lastColRow[c]
                union((r,c), (row, c))

            lastRowCol[r] = c
            lastColRow[c] = r

        removedStones = 0
        for stone in stones:
            if reps[tuple(stone)] != tuple(stone):
                removedStones += 1
        
        return removedStones
        
        