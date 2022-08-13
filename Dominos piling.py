def maxDominos(n, m):
    return (n*m)//2
 
if __name__ == '__main__':
    board = input(" Enter domino board Dimensions. (separate with comma ',') ").split(',')
    print(maxDominos(int(board[0]), int(board[1])))
