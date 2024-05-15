var directions = [4][2]int {
    {0,  1},
    {0, -1},
    {1,  0},
    {-1, 0},
}

func isInbound(grid [][]int, row int, col int) bool {
    return 0 <= row && row < len(grid) && 0 <= col && col < len(grid[0]);
}

// It's just a matter of traversing the array
func islandPerimeter(grid [][]int) int {
    perimeter := 0;

    for row, _ := range(grid) {
        for col, _ := range(grid[0]) {
            // check if it is inbound, and has water.
            if (grid[row][col] == 1) {
                // check if it's four sides
                for _, dir := range directions {
                    newRow, newCol := dir[0], dir[1];
                    if (!isInbound(grid, row + newRow, col + newCol) || grid[row + newRow][col + newCol] == 0) {
                        perimeter ++;
                    }
                }
                
            }
        }
    }

    return perimeter;
}
