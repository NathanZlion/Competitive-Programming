class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        neighbors = [(-1,0),(0,-1),(1,0),(0,1)]
        
        rows, cols = len(grid), len(grid[0])
        
        stack = []

        # top and bottom boundary
        firstRow = firstCol = 0
        lastRow , lastCol = rows-1, cols-1

        for col in range(cols):
            if grid[firstRow][col] == 1:
                stack.append((firstRow, col))
            
            if grid[lastRow][col] == 1:
                stack.append((lastRow, col))

        # left and right boundary
        for row in range(rows):
            if grid[row][firstCol] == 1:
                stack.append((row, firstCol))
            
            if grid[row][lastCol] == 1:
                stack.append((row, lastCol))
        
        while stack:
            currRow, currCol = stack.pop()
            
            grid[currRow][currCol] = 0

            for neighbor in neighbors:
                neighborRow, neighborCol = neighbor
                neighborRow += currRow
                neighborCol += currCol

                if neighborRow < 0 or neighborCol < 0 or neighborRow >= rows or neighborCol >= cols:
                    continue
                
                if grid[neighborRow][neighborCol] == 1:
                    stack.append((neighborRow, neighborCol))
                
        ctr = 0
        for row in range(rows):
            for col in range(cols):
                ctr += grid[row][col]
        
        return ctr            
        
        
        
                