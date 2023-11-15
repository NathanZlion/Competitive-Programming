class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        count = [0 for _ in range(n)]
        available_time = [0 for _ in range(n)]
        meetings.sort()

        curr_time = 0
        for ptr in range(len(meetings)):
            start, end = meetings[ptr]

            # if the current meeting is not ready yet, fast forward time
            if start > curr_time:
                curr_time = start

            # find a meeting room for this meeting
            next_meeting_room = -1
            for meeting_room in range(n):
                if available_time[meeting_room] <= curr_time:
                    next_meeting_room = meeting_room
                    break

            # if there is not available room, fast forward to when the soonest room finishes
            if next_meeting_room == -1:
                next_meeting_room = available_time.index(min(available_time))
                curr_time = available_time[next_meeting_room]
            
            # add the meeting into the room
            duration = end - start
            available_time[next_meeting_room] = curr_time + duration
            count[next_meeting_room] += 1

        max_meeting_room = 0
        for meeting_room in range(1, n):
            if count[meeting_room] > count[max_meeting_room]:
                max_meeting_room = meeting_room

        return max_meeting_room