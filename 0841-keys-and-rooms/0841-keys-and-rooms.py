class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        isLocked = [True for _ in range(N)]
        isLocked[0] = False
        queue = deque()
        queue.append(0)

        while len(queue) > 0:
            currKey = queue.popleft()

            for roomKey in rooms[currKey]:
                if isLocked[roomKey]:
                    isLocked[roomKey] = False
                    queue.append(roomKey)

        for index in range(N):
            if isLocked[index]:
                return False

        return True

