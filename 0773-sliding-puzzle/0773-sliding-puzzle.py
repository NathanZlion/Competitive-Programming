class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # convert the 2d board into a 1d board
        flatBoard = [col for row in board for col in row]
        solvedState = [1, 2, 3, 4, 5, 0]

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        def __hash(flatBoard : List[int]) -> int:
            hashVal = 0
            for index in range(6):
                hashVal *= 10
                hashVal += flatBoard[index]
            
            return hashVal


        queue = deque()
        queue.append(flatBoard)

        visited = set()
        visited.add(__hash(flatBoard))

        numberOfSwaps = 0
        
        while len(queue) > 0:
            for _ in range(len(queue)):

                flatBoard = queue.popleft()
                if flatBoard == solvedState:
                    return numberOfSwaps
                
                zeroPos = flatBoard.index(0)
                
                for neighbor in neighbors[zeroPos]:
                    # swap zero with neighbor
                    flatBoard[zeroPos], flatBoard[neighbor] = flatBoard[neighbor], flatBoard[zeroPos]
                    hashVal : int = __hash(flatBoard)

                    if hashVal not in visited:
                        queue.append(flatBoard.copy())
                        visited.add(hashVal)
                    
                    # revert the swap
                    flatBoard[zeroPos], flatBoard[neighbor] = flatBoard[neighbor], flatBoard[zeroPos]
                    
                
            numberOfSwaps += 1
        
        
        return -1
