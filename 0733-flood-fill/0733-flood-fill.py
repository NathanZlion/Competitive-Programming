class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        stack = [(sr,sc)]
        neighbors = [(0,1), (1,0), (-1,0), (0,-1)]
        explored = set()
        floodColor = image[sr][sc]
        isExplored= lambda row, col: (row, col) in explored
        
        isInbound = lambda r, c: 0 <= r < len(image) and 0 <= c < len(image[0])
        isValid = lambda r,c : isInbound(r,c) and image[r][c] == floodColor

        while stack:
            row, col = stack.pop()
            if image[row][col] != floodColor or isExplored(row, col):
                continue
            explored.add((row, col))
            image[row][col] = color
            
            for neighbor in neighbors:
                r, c = neighbor
                if isValid(r+row, c+col):
                    stack.append((r+row, c+col))

        return image
                    
            