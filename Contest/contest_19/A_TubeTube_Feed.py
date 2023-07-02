i = int(input())

for _ in range(i):
    n, t = map(int, input().split())
    dur = list(map(int, input().split()))
    ent = list(map(int, input().split()))

    # do your thing and print just 1 number.
    max_utility_index = -1
    max_utility = 0

    # iterating the videos
    for index in range(n):
        rem_time = t - dur[index] - index
        if rem_time >= 0 and ent[index] > max_utility:
            max_utility_index = index + 1
            max_utility = ent[index]
    
    print(max_utility_index)

