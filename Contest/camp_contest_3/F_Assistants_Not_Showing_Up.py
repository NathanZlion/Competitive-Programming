

n,m = list(map(int, input().split()))
days = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = list(map(int, input().split()))
    days[a] += 1
    days[b+1] -= 1
days[-1] = 0

for index in range(n):
    days[index] += days[index-1]

days.pop()

def hasZeros():
    for day in days:
        if day == 0:
            return False
    return True

if hasZeros():
    print('NO')
else:
    print('YES')
