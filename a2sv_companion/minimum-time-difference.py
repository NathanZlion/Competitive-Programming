class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def num_of_minutes(time: str) -> int:
            hours, minutes = time.split(":")
            hours = int(hours)
            minutes = int(minutes)
            MINUTES_IN_HOURS = 60

            return hours * MINUTES_IN_HOURS + minutes

        def min_dce(time1: int, time2: int, twenty_four_hours: int) -> int:
            difference = abs(time2 - time1)
            if difference > twenty_four_hours // 2:
                return twenty_four_hours - difference

            return difference

        total_time = "24:00"
        twenty_four_hours = num_of_minutes(total_time)
        times = sorted([num_of_minutes(time) for time in timePoints])
        times.append(times[0])

        return min([min_dce(times[i+1], times[i], twenty_four_hours) for i in range(len(timePoints))])
