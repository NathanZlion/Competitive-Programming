class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        result = [[0 for i in range(n+2)] for j in range(n+2)]
        
        for query in queries:
            row1 = query[0]+1
            col1 = query[1]+1
            row2 = query[2]+1
            col2 = query[3]+1
            
            result[row1][col1] += 1
            result[row1][col2+1] -= 1
            result[row2+1][col1] -= 1
            result[row2+1][col2+1] += 1
            
        for r in range(1, n+2):
            for c in range(1, n+2):
                result[r][c] = result[r-1][c] + result[r][c-1] - result[r-1][c-1] + result[r][c]
        
        ans = []
        
        for r in range(1,n+1):
            mat = result[r]
            ans.append(mat[1:n+1])
        
        return ans
            
            
            
        
        