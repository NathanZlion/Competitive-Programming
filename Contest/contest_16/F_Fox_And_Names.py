

from collections import defaultdict


n = int(input())

names = [input() for _ in range(n)]

# return lexological order if exists
adjList = defaultdict(list)

