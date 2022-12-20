class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        """roomstate: True => Open, False => Closed """
        roomState  = {}

        for i in range(len(rooms)):
            roomState[i] = False

        roomState[0] = True     # room 0 is open

        def unlock(roomNum):
            roomState[roomNum] = True

            for key in rooms[roomNum]:
                if not roomState[key]:
                    unlock(key)
        
        unlock(0)
        for isOpen in roomState.values():
            if (not isOpen):
                return False

        return True
