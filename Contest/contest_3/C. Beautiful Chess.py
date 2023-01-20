

t =  int(input())


def bishopIndex(board):
    for row in range(1, 7):
        for col in range(1, 7):
            if (board[row][col] == "#"):
                top_left = board[row -1][col -1]
                top_right = board[row -1][col +1]
                bot_left = board[row +1][col -1]
                bot_right = board[row +1][col +1]

                if (top_left == "#" and top_right == "#" and bot_left == "#" and bot_right == "#"):
                    return [row, col]

for i in range(t):
    board = []
    input() 
    for i in range(8):
        board.append(input())
        
    res= bishopIndex(board)
    print(res[0]+1,res[1]+1)  

    



