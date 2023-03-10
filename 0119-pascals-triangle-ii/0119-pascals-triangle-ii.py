class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1 for _ in range(rowIndex+1)]

        above = self.getRow(rowIndex-1)        
        res = [1 for _ in range(rowIndex+1)]

        for index in range(rowIndex-1):
            res[index+1] = above[index]+above[index+1]

        return res
