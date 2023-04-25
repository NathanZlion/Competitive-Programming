

x = int(input())

added = 0

while x:
    if x%2 == 1:
        x -= 1
        added += 1
    x //= 2


print(added)
