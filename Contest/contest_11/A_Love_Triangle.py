

n = int(input())
f = list(map(int, input().split()))
explored = set()


def explore(index):
    arr = [index+1]
    curr = index
    for _ in range(3):
        arr.append(f[curr])
        curr = f[curr]-1
    return arr[0] == arr[-1]
    

hasTriangle = False
for index in range(n):
    if explore(index):
        hasTriangle = True
        break

print("YES" if hasTriangle else "NO")
    
