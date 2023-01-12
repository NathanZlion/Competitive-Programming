

n = int(input())

scores =  list(map(int, input().split()))


min_ = scores[0]
max_ = scores[0]

# strictly max
# strictly min

amazNum = 0

for i in range(1, len(scores)):
    score = scores[i]
    if score < min_:
        min_ = score
        amazNum += 1

    elif score > max_:
        max_ = score
        amazNum += 1

print(amazNum)

