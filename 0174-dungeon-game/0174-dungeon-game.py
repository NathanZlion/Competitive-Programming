class Solution:        
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = defaultdict(lambda : -inf)
        dp[(rows,cols-1)] = 0 

        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                dp[(row,col)] = max(dp[(row+1,col)], dp[(row,col+1)])
                dp[(row,col)] = min(dungeon[row][col] + dp[(row,col)], 0)

        return abs(dp[(0,0)])+ 1
