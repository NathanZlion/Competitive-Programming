numOfSquares = int(input())
colors = list(map(int, input().split()))
uniqueColors = set(colors)

print(len(uniqueColors) -1)