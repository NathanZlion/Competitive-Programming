rank = {"A": 0, "B": 0, "C": 0}

for _ in range(3):
    result = input()

    if ">" in result:
        val1,val2 = result.split(">")
        rank[val1] += 1
        rank[val2] -= 1
    
    else:
        val1,val2 = result.split("<")
        rank[val2] += 1
        rank[val1] -= 1

if (len(set(rank.values()))) == 3:
    res = ["A", "B", "C"]
    res.sort(key=lambda x: rank[x])

    print("".join(res))
else:
    print("Impossible")

