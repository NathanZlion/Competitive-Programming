class Solution:
    
    def eucledianDistance(self, row: int, col: int) -> int:
        return (row ** 2) + (col ** 2)
    
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        furthestEucledianDistance = 0

        # make the obstacles a set for an 0(1) lookup
        obstacles = set([(col, row) for row, col in obstacles])

        directions = [
            (1,  0),  # up
            (0,  1),  # right
            (-1, 0),  # down
            (0, -1)   # left
        ]
        
        currRow, currCol, currDirection = 0, 0, 0
        for command in commands:
            # turn left or right
            if command < 0:
                if command == -1:
                    currDirection += 1
                else:
                    currDirection -= 1
                currDirection %= 4
            else:
                dirRow, dirCol = directions[currDirection]
                for _ in range(command):
                    if (currRow + dirRow, currCol + dirCol) in obstacles:
                        break

                    currRow += dirRow
                    currCol += dirCol

                furthestEucledianDistance = max(furthestEucledianDistance, self.eucledianDistance(currRow, currCol))
                print(currRow, currCol)

        return furthestEucledianDistance
