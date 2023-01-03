
from collections import Counter

t = int(input())

for i in range(t):
    n, cost = tuple(map(int, input().split()))
    a = list(map(int, input().split()))       # orbit of ith planet
    planetsAtOrbit = Counter(a)

    min_cost = 0
    for orbit in planetsAtOrbit:
        if planetsAtOrbit[orbit] == 1:
            min_cost += 1
        else:
            if (planetsAtOrbit[orbit]) > cost:
                min_cost += cost
            else:
                min_cost += planetsAtOrbit[orbit]

    print(min_cost)
