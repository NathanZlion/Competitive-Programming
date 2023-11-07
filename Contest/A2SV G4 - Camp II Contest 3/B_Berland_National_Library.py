numOfRecords = int(input())

logs = []
for _ in range(numOfRecords):
    sign, id = input().split()
    logs.append((sign, id))

visited = set()

count = 0
maxCount = 0

for sign, id in logs:
    if id in visited:
        continue
    if sign == "-":
        count += 1
        maxCount = count

    visited.add(id)

for sign, id in logs:
    if sign == '+':
        count += 1
    else:
        count -= 1

    maxCount = max(count, maxCount)

print(maxCount)