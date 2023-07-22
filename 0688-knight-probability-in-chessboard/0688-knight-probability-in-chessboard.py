from collections import deque

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2,-1), (-2, 1), ( 2,-1), (2, 1), (-1,-2), ( 1,-2), (-1, 2), (1, 2)]
        queue = deque()

        prev_count = {}
        curr_count = {}
        queue.append((row, column))
        prev_count[(row, column)] = 1

        def is_inbound(row, col):
            return 0 <= row < n and 0 <= col < n

        for number_of_moves in range(k):
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                prev = prev_count[(curr_row, curr_col)]

                for r, c in moves:
                    new_row, new_Col = curr_row+r, curr_col+c
                    if is_inbound(new_row, new_Col):
                        if (new_row, new_Col) in curr_count:
                            curr_count[(new_row, new_Col)] += prev
                        else:
                            curr_count[(new_row, new_Col)] = prev
                            queue.append((curr_row+r, curr_col+c))

            # then swap curr to prev and clear prev
            prev_count = curr_count
            curr_count = {}


        total_count = 8**k
        inbound_count = sum(prev_count.values())

        return inbound_count/total_count