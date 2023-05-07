

from heapq import heapify, heappop, heappush


t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    sociability = []

    for index, social in enumerate(s):
        if social > 0:
            sociability.append((social*-1, index+1))

    heapify(sociability)

    conversation_count = 0
    conversations = []

    while len(sociability) >= 2:
        conversation_count += 1
        s1, index1 = heappop(sociability)
        s2, index2 = heappop(sociability)
        conversations.append((min(index1, index2), max(index1, index2)))

        if s1*-1 > 1:
            heappush(sociability, (s1+1, index1))
        if s2*-1 > 1:
            heappush(sociability, (s2+1, index2))

    
    print(conversation_count)

    for index1, index2 in conversations:
        print(index1, index2)

    

