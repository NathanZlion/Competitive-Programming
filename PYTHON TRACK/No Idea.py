
input()

arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0
for i in arr:
    if i in a:
        happiness += 1
    elif i in b:
        happiness -= 1

print(happiness)
