class Solution:
    def racecar(self, target: int) -> int:
        
        # {(speed, position, numberOfMoves)}
        queue = deque()
        queue.append((1, 0))
        visited = set()
        visited.add((1, 0))


        numOfMoves = 0

        while queue:
            for _ in range(len(queue)):
                speed, position = queue.popleft()

                if position == target:
                    return numOfMoves

                if (1 if speed <= 0 else -1, position) not in visited and position > 0:
                    visited.add((1 if speed <= 0 else -1, position))
                    queue.append((1 if speed <= 0 else -1, position))    # taking R move

                if not (speed*2, position+speed) in visited:
                    visited.add((speed*2, position+speed))
                    queue.append((speed*2, position+speed))      # taking A move

            numOfMoves += 1