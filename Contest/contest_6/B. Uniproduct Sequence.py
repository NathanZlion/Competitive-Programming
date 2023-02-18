

n = int(input())

arr = list(map(int, input().split()))

# for each compute distance from 1 or -1
# for each store sign
# then if sign gets minus find the one with smallest distance and if negative make it positive

sign = []
dist = []
count = 0
for num in arr:
    if num > 1:
        sign.append(1)
        dist.append(num -1)
        count += 1
    elif num< 1:
        sign.append(0)
        dist.append(-num -1)
        count += 1
    elif num == 0:
        sign.append(1)
        dist.append(1)
        count += 1

positive = True
for s in sign:
    if s == 0:
        positive = not positive

if positive:
    print(count)
else:
    for i in range()


