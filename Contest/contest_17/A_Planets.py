
from collections import defaultdict

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    orbits = list(map(int, input().split()))

    count = defaultdict(int)
    
    for orbit in orbits:
        count[orbit] += 1

    cost = 0
    for orbit, freq in count.items():
        cost += min(c, freq)
    
    print(cost)
