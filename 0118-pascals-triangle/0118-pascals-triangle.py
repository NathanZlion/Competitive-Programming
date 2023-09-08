class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1,numRows+1):
            res.append([1 for _ in range(i)])
        
        for row in range(2,numRows):
            for col in range(1,row):
                res[row][col] = res[row-1][col-1] + res[row-1][col]
        
        return res
