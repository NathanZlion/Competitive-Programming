

n,t = map(int, input().split())
arr = list(map(int, input().split()))
possible = False
curr = 0

while True:
    if curr > t-1:
        break

    if curr == t-1:
        possible = True
        break
    curr += arr[curr]


print("YES" if possible else "NO")
