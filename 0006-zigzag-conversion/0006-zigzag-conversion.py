class Solution:
    def convert(self, s: str, numRows: int) -> str:        
        res = [[] for _ in range(numRows)]
        
         # up and down
        directions = [1, -1]
        currDirection = 0
        currRow = 0
        
        for char in s:
            res[currRow].append(char)
            if not (0 <= currRow + directions[currDirection] < numRows):
                currDirection = (currDirection + 1) % 2
            
            currRow += directions[currDirection]
        
        return "".join(["".join(row) for row in res])
