class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        totalRows = len(mat)
        totalCols = len(mat[0])
    
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def isInbound(row, col):
            return 0 <= row < totalRows and 0 <= col < totalCols

        queue = deque()

        for row in range(totalRows):
            for col in range(totalCols):
                
                # add all 0 locations to queue as they are the sources
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = 10_000

        while len(queue) > 0:
            row, col = queue.popleft()

            for r, c in directions:
                # if less cost found this way, update ad explore from there
                if isInbound(row + r, col + c) and mat[row+r][col+c] > mat[row][col]+1:
                    mat[row+r][col+c] = mat[row][col]+1
                    queue.append((row+r, col+c))


        return mat
