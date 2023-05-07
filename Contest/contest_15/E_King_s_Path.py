
from collections import defaultdict, deque

start_row, start_col, end_row, end_col = map(int, input().split())
n = int(input())
is_allowed = defaultdict(bool)

for _ in range(n):
    row, a, b = map(int, input().split())

    for col in range(a, b+1):
        is_allowed[(row, col)] = True


def explore():
    directions = [(0,1), (1,0), (0,-1) ,(-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
    visited = set()
    visited.add((start_row, start_col))
    queue = deque()
    queue.append((start_row, start_col))

    number_of_moves = 0
    while len(queue) > 0:
        for _ in range(len(queue)):
            row, col = queue.popleft()

            if (row, col) == (end_row, end_col):
                return number_of_moves

            # discovering all neighbors
            for new_row, new_col in directions:
                new_row += row
                new_col += col

                if is_allowed[(new_row, new_col)] and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))

        number_of_moves += 1

    return -1

print(explore())

