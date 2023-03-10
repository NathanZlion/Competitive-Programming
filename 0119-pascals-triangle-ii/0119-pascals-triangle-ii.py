class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1 for _ in range(rowIndex+1)]

        above = self.getRow(rowIndex-1)        
        res = [1 for _ in range(rowIndex+1)]

        for index in range(1, rowIndex):
            res[index] = above[index-1]+above[index]

        return res
