class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def representative(coord):
            while coord != reps[coord]:
                coord = reps[coord]

            return coord

        def union(coord1, coord2):
            rep1 = representative(coord1)
            rep2 = representative(coord2)
            
            # merge to rep1
            if size[rep1] > size[rep2]:
                reps[rep2] = rep1
                size[rep1] = max(size[rep1], size[rep2] + 1)

            else:
                reps[rep1] = rep2
                size[rep2] = max(size[rep2], size[rep1] + 1)


        reps = {(a,b): (a,b) for a,b in stones}
        size = {(a,b): 1 for a,b in stones}
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
        
        