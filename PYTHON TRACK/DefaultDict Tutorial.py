
from collections import defaultdict


nm = list(map(int, input().split()))
n, m = nm[0], nm[1]

dict_a = defaultdict(list)

for i in range(n):
    dict_a[input()].append(str(i+1))

for j in range(m):
    char=input()
    if (dict_a[char]):
        print(" ".join(dict_a[char]))
    else:
        print("-1")
