

from collections import defaultdict

n, m = map(int, input().split())

reps = {i:i for i in range(1, n+1)}

def find(node):
    while node != reps[node]:
        node = reps[node]
    
    return node


def union(node, theRep):
    while node != reps[node]:
        nxt = reps[node]
        reps[node] = theRep
        node = nxt

    reps[node] = theRep

for _ in range(m):
    arr = list(map(int, input().split()))

    for index in range(1, len(arr)-1):
        union(arr[index], find(arr[index+1]))

groupAmount = defaultdict(int)

for node in range(1,n+1):
    groupAmount[find(node)] += 1

ans = [groupAmount[find(node)] for node in range(1, n+1)]

print(*ans)
