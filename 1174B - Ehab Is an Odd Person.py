

n = int(input())

arr = list(map(int, input().split()))

even = False
odd = False

for num in arr:
    if num%2:
        odd = True
    else:
        even = True

if odd and even:
    arr.sort()

print(*arr)
