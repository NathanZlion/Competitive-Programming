class Solution:
    @cache
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prevRow = self.getRow(rowIndex-1)
        currRow = [1 for _ in range(rowIndex+1)]

        for i in range(1, rowIndex):
            currRow[i] = prevRow[i-1] + prevRow[i]

        return currRow