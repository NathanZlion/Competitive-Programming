from collections import defaultdict


k = int(input())
rooms = list(map(int, input().split()))

freq = defaultdict(int)

for i in rooms:
    freq[i] += 1

for key in freq.keys():
    if freq[key] != k:
        print(key)
        break
