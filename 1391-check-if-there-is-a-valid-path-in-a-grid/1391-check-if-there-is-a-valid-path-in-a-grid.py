class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        rowLength = len(grid)
        colLength = len(grid[0])

        reps = [i for i in range(colLength * rowLength)]
        
        def representative(node):
            while reps[node] != node:
                node = reps[node]

            return node

        def unify(node1, node2):
            commonRep = representative(node2)

            while reps[node1] != node1:
                next = reps[node1]
                reps[node1] = commonRep
                node1 = next

            reps[node1] = commonRep

        def toInt(row, col):
            nonlocal colLength
            return row * colLength + col

        def toRowCol(num):
            return num // colLength, num % colLength
        
        def isInbound(num):
            return 0 <= num < colLength * rowLength
        
        left = {1, 4, 6}
        right = {1, 3, 5}
        up = {2, 3, 4}
        down = {2, 5, 6}

        validNeighbors = {
            1: [left, right],
            2: [up, down],
            3: [left, down],
            4: [down, right],
            5: [left, up],
            6: [up, right]
        }

        streetToMove = {
            1: (-1, 1),
            2: (-colLength, colLength),
            3: (-1, colLength),
            4: (1, colLength),
            5: (-1, -colLength),
            6: (-colLength, 1),
        }
        
        for row in range(rowLength):
            for col in range(colLength):
                curr = toInt(row, col)
                first, second = streetToMove[grid[row][col]]
                first += curr
                second += curr
                firstRow, firstCol = toRowCol(first)
                secondRow, secondCol = toRowCol(second)
                
                validFirst, validSecond = validNeighbors[grid[row][col]]

                if isInbound(first) and grid[firstRow][firstCol] in validFirst:
                    # make a connection between current and the first
                    unify(curr, first)
                    
                    
                if isInbound(second) and grid[secondRow][secondCol] in validSecond:
                    # make a connection between current and the second
                    unify(curr, second)

        return representative(toInt(0,0)) == representative(toInt(rowLength-1, colLength-1))

        