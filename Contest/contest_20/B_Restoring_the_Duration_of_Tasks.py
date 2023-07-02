
t = int(input())

for _ in range(t):
    n = int(input())

    s = list(map(int, input().split())) # The time task was given
    f = list(map(int, input().split())) #  The completed time

    # required is the duration ot the task
    for index in range(1, len(s)):
        if s[index] < f[index-1]:
            s[index] = f[index-1]
    
    duration = [f[index] - s[index] for index in range(len(s))]
    print(*duration)


