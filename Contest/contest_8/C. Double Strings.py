
from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())

    strings = [input() for _ in range(n)]
    
    dc = defaultdict(int)
    for string in strings:
        dc[string] += 1
    
    
    res = []
    for string in strings:
        if not string:
            res.append("0")
            continue

        has = False
        for i in range(1,len(string)):
            left = string[:i]
            right = string[i:]
            if (left in dc and right in dc):
                has = True
        if has:
            res.append("1")
        else:
            res.append("0")
    print("".join(res))
