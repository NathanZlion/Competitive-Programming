class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        isInbound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        neighbors = [(-1,0),(0,-1),(1,0),(0,1)]

        def isLand(coordinate) -> bool:
            r,c = coordinate

            if not isInbound(r,c):
                return False
            
            return grid[r][c] == 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += 4

                    for neighbor in neighbors:
                        neighbor = (neighbor[0] + row, neighbor[1] + col)
                        if isLand(neighbor):
                            perimeter -= 1

        return perimeter
        
        
            