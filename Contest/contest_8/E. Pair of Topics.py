

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

goodPairs = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i]+a[j]>b[i]+b[j]:
            goodPairs += 1

print(goodPairs)
