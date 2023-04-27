class Solution(object):
    def canVisitAllRooms(self, rooms):
        openedRooms = set()
        queue = deque()
        queue.append(0)
        openedRooms.add(0)

        while len(queue) > 0:
            currKey = queue.popleft()

            for roomKey in rooms[currKey]:
                if roomKey not in openedRooms:
                    openedRooms.add(roomKey)
                    queue.append(roomKey)
        
        return len(openedRooms) == len(rooms)
