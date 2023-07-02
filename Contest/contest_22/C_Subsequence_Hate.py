
t = int(input())


mask = [0] * 1000
possibleMasks = [mask]

for index in range(1000):
    mask[index] = 1
    possibleMasks.append(mask.copy())

for index in range(1000):
    mask[index] = 0
    possibleMasks.append(mask.copy())


for _ in range(t):
    s = input()
    n = len(s)
    arr = [int(char) for char in s]

    minNumberOfSwaps = float('inf')
    for mask in possibleMasks:
        numberOfSwaps = 0
        for index in range(n):
            if int(s[index]) != mask[index]:
                numberOfSwaps += 1

        minNumberOfSwaps = min(minNumberOfSwaps,  numberOfSwaps)

    print(minNumberOfSwaps)

# n**2 time complexity
# O(1) space complexity
