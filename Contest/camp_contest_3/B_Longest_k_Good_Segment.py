
from collections import defaultdict

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
freq = defaultdict(int)

longest_segment = [0,0]

for right in range(n):
    freq[arr[right]] += 1

    while len(freq) > k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            del freq[arr[left]]

        left += 1

    if longest_segment[1] - longest_segment[0] <= right - left:
        longest_segment = [left+1, right+1]

print(*longest_segment)    
