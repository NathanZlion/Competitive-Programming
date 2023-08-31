class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Create a list to track the maximum reach for each position
        max_reach = [0] * (n + 1)

        # Calculate the maximum reach for each tap
        for i in range(len(ranges)):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])

            # Update the maximum reach for the leftmost position
            max_reach[start] = max(max_reach[start], end)
        
        taps = 0
        curr_end = 0
        next_end = 0

        # Iterate through the garden
        for i in range(n + 1):
            if i > next_end:
                return -1

            if i > curr_end:
                taps += 1
                curr_end = next_end

            next_end = max(next_end, max_reach[i])

        return taps