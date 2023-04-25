
from collections import defaultdict

n = int(input())

immediate_manager = []
for _ in range(n):
    immediate_manager.append(int(input()))


subordinates = defaultdict(list)
for index in range(n):
    if immediate_manager[index] != -1:
        try:
            subordinates[immediate_manager[index]].append(index+1)
        except:
            pass

explored = set()

def dfs(num):
    explored.add(num)
    max_depth = 0

    for subordinate in subordinates[num]:
        max_depth = max(max_depth, dfs(subordinate))

    return 1 + max_depth

res = 0

for index in range(1,n+1):
    if not index in explored:
        res = max(res, dfs(index))

print(res if n > 1 else 1)

