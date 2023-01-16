class Solution(object):
    def isToeplitzMatrix(self, matrix):
      
        diagonals = defaultdict(list)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                diagonals[row-col].append(matrix[row][col])
            
        
        for diagonal in diagonals.values():
            for i in range(len(diagonal)-1):
                if diagonal[i] != diagonal[i+1]:
                    return False
        
        return True
                
