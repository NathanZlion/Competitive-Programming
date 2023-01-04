class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """

        row_size = king[0]
        col_size = king[1]
        for queen in queens:
            row_size = max(row_size, queen[0])
            col_size = max(col_size, queen[1])


        validQueens=[]

        def checkLeft():
            # move left from king till left end is reached or you get a queen
            row = king[0]
            col = king[1]-1
            while col >= 0:
                if [row, col] in queens:
                    validQueens.append([row,col])
                    break
                col -= 1

        def checkRight():
            # move right from king till right end is reached or you get a queen
            row = king[0]
            col = king[1]+1
            while col <= col_size:
                if [row, col] in queens:
                    validQueens.append([row,col])
                    break
                col += 1

        def checkBottom():
            # move bottom from king till bottom end is reached or you get a queen
            row = king[0]+1
            col = king[1]
            while row <= row_size:
                if [row, col] in queens:
                    validQueens.append([row,col])
                    break
                row += 1
    
        def checkTop():
            # move top from king till top end is reached or you get a queen
            row = king[0]-1
            col = king[1]
            while row >= 0:
                if [row, col] in queens:
                    validQueens.append([row,col])
                    break
                row -= 1

        def checkTopRight():
            # move top and right from king till end is reached or you get a queen
            row = king[0]-1
            col = king[1]+1
            while row >= 0 and col <= col_size:
                if [row, col] in queens:
                    validQueens.append([row,col])
                    break
                row -= 1
                col += 1

        def checkTopLeft():
            # move up and left from king till end is reached or you get a queen        
            row = king[0]-1
            col = king[1]-1
            while row >= 0 and col >= 0:
                if [row, col] in queens:
                    validQueens.append([row,col])
                    break
                row -= 1
                col -= 1

        def checkBottomLeft():
            # move down and left from king till end is reached or you get a queen           
            row = king[0]+1
            col = king[1]-1
            while row <= row_size and col >= 0:
                if [row, col] in queens:
                    validQueens.append([row,col])
                    break
                row += 1
                col -= 1

        def checkBottomRight():
            # move down and right from king till end is reached or you get a queen   
            row = king[0]+1
            col = king[1]+1
            while row <= row_size and col <= col_size:
                if [row, col] in queens:
                    validQueens.append([row,col])
                    break
                row += 1
                col += 1
        
        checkLeft()
        checkRight()
        checkTop()
        checkBottom()
        checkTopLeft()
        checkTopRight()
        checkBottomLeft()
        checkBottomRight()
        
        return validQueens
