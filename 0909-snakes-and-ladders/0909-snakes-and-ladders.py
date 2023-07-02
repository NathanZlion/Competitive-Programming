class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        linearBoard = [0]
        reverse = False
        n =  len(board)

        for row in range(n-1, -1, -1):
            cols = range(n) if not reverse else range(n-1, -1, -1)
            for col in cols:
                linearBoard.append(board[row][col])

            reverse = not reverse
        
        for i in range(1, n**2+1):
            if linearBoard[i] == -1:
                linearBoard[i] = i

        queue = deque()
        queue.append((1, 0))
        
        visited = set()
        visited.add(1)

        while queue:
            start, cost = queue.popleft()

            if start == n**2:
                return cost

            for i in range(start+1, min(start+7, n*n+1)):
                destination = linearBoard[i]

                if destination not in visited:
                    visited.add(destination) 
                    queue.append((destination, cost+1))

        return -1