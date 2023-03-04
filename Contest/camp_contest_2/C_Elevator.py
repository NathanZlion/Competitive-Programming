

t = int(input())

total_floors = 4

for _ in range(t):
    wt, et, ef = tuple(map(int, input().split()))
    min_ = float('inf')

    # walk_only_time
    walk_only_time = wt * 4

    for walk_floors in range(4):
        elevator_floors = total_floors - walk_floors
        elevator_waiting_time = abs(ef- walk_floors) * et
        walking_time = walk_floors * wt
        elevator_time = elevator_floors * et

        time_taken = elevator_waiting_time + walking_time + elevator_time

        min_ = min(min_, time_taken)

    print(min(min_, walk_only_time))
