
# count the number of roads in the city

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

num_of_roads = 0

for i in range(n):
    for j in range(i):
        if arr[i][j] == 1:
            num_of_roads += 1

print(num_of_roads)
