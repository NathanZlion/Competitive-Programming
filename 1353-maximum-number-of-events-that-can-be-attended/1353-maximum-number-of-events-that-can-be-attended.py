
from heapq import heappop, heappush

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort()
        heap = []
        attendedEventsCnt = 0
        index, numberOfEvents = 0, len(events)
        currDay = 0  # current day

        while index < numberOfEvents or heap:
            if not heap:
                # jump to the next available event start day
                currDay = events[index][0]

            # push all events we can possibly attend
            while index < numberOfEvents and currDay >= events[index][0]:
                # push to heap by the end day
                heappush(heap, events[index][1])
                index += 1

            # attend this one event
            heappop(heap)
            attendedEventsCnt += 1
            currDay += 1

            # remove all impossible-to-attend events
            # whose end day is beofre current day
            while heap and heap[0] < currDay:
                heappop(heap)


        return attendedEventsCnt
