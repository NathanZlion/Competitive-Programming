
from collections import defaultdict
from heapq import heapify, heappop

# number of characters in overcity, number of pairs of friends
n, m = map(int, input().split())

gold_needed = list(map(int, input().split()))
for index, gold in enumerate(gold_needed):
    gold_needed[index] = (gold, index+1)

heapify(gold_needed)

friends = defaultdict(list)

# make adjecency list of all friends
for _ in range(m):
    character_a, character_b = map(int, input().split())
    friends[character_a].append(character_b)
    friends[character_b].append(character_a)

heard = set()
golds_spent = 0

# the minimum gold to spread the rumor completely
def bribe(index):
    stack = [index]
    while stack:
        curr = stack.pop()

        for friend in friends[curr]:
            if not friend in heard:
                heard.add(friend)
                stack.append(friend)

# take the minimum one every time and bribe them 
# if they haven't heard yet
while gold_needed:
    gold, index = heappop(gold_needed)
    if not index in heard:
        heard.add(index)
        golds_spent += gold
        bribe(index)

print(golds_spent)
