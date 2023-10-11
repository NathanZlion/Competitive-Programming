class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # North, East, South, West
        directions = [(0,  1), (1,  0), (0, -1), (-1, 0)]
        direction = 0
        coordinate = [0, 0]

        def execute(instruction, coordinate, direction):

            x, y = directions[direction]

            if instruction == "G":
                coordinate = [coordinate[0] + x, coordinate[1]+y]

            elif instruction == "L":
                direction -= 1
                direction %= 4

            elif instruction == "R":
                direction += 1
                direction %= 4
            
            return coordinate, direction    

        for instruction in instructions:
            coordinate, direction = execute(instruction, coordinate, direction)

        final_x, final_y = coordinate

        if (final_x, final_y) != (0, 0) and direction == 0:
            return False

        return True
