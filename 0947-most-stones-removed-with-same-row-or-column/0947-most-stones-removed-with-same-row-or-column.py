class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def toInt(row, col):
            MAXCOL = 10_000
            return MAXCOL*row + col

        def representative(num):
            while num != reps[num]:
                num = reps[num]
            
            return num

        def union(num1, num2):
            rep1 = representative(num1)
            rep2 = representative(num2)
            
            reps[rep1] = rep2

        reps = {toInt(a,b): toInt(a,b ) for a,b in stones}
        lastRowCol = {}
        lastColRow = {}

        for r,c in stones:
            if r in lastRowCol:
                col = lastRowCol[r]
                union(toInt(r,c), toInt(r, col))

            if c in lastColRow:
                row = lastColRow[c]
                union(toInt(r,c), toInt(row, c))

            lastRowCol[r] = c
            lastColRow[c] = r

        removedStones = 0
        for r,c in stones:
            num = toInt(r,c)
            if reps[num] != num:
                removedStones += 1
        
        return removedStones
        
        