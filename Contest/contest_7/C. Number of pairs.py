


n = int(input())
boys = list(map(int, input().split()))

m = int(input())
girls = list(map(int, input().split()))


boys.sort()
girls.sort()

ptr1 = 0
ptr2 = 0
pairs = 0
while ptr1 < n and ptr2 < m:
    if abs(boys[ptr1]  - girls[ptr2]) < 2:
        pairs += 1
        ptr1 += 1
        ptr2 += 1
    elif boys[ptr1] > girls[ptr2]:
        ptr2 += 1
    else:
        ptr1 += 1

print(pairs)
