
n, d = map(int, input().split())

# initially 0 acquintance for all people
acq = {i:0 for i in range(1,n+1)}
reps = {i:i for i in range(1, n+1)}
maximum_acq = 0

def find(node):
    while node != reps[node]:
        node = reps[node]

    return node

def union(node1, node2, maximum_acq):
    rep1 = find(node1)
    rep2 = find(node2)

    if rep1 == rep2:
        return maximum_acq

    reps[rep2] = rep1
    acq[rep1] += acq[rep2] + 1

    return max(maximum_acq, acq[rep1])

for _ in range(d):
    p1, p2 = map(int, input().split())

    next_big_acq = union(p1, p2, maximum_acq)

    print(maximum_acq)
