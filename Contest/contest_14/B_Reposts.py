
from collections import defaultdict


n = int(input())
# names are case insensitive

adjList = defaultdict(list)

def toLowercase(s:str): return s.lower()

for _ in range(n):
    # take input
    name1, _ , name2 = map(toLowercase ,input().split())
    adjList[name2].append(name1)

def dfs(name: str):
    maxRepost = 0

    for neighbor in adjList[name]:
        maxRepost = max(maxRepost, dfs(neighbor))

    return maxRepost+1

print(dfs("polycarp"))