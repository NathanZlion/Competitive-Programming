class Solution:
    
    def toMinutes(self, time:str) -> int:
        hour, mins = time.split(":")
        minutes = (int(hour) * 60)+ int(mins)

        return minutes

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # happen on the same day
        # HH:MM
        # convert it to a second representation

        start1, end1 = [self.toMinutes(time) for time in event1]
        start2, end2 = [self.toMinutes(time) for time in event2]

        if start1 < start2:
            return end1 >= start2

        if start1 >= start2:
            return end2 >= start1