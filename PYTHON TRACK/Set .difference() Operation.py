n = int(input())
e = set(map(int, (input().split())))
m = int(input())
f = set(map(int, (input().split())))

res = 0

for i in e:
    if not i in f:
        res += 1


print(res)
