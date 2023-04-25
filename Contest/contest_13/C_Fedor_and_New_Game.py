
# m players
# n types of soliders

n,m,k = map(int, input().split())
army = [int(input()) for _ in range(m+1)]

friends_count = 0

# bitCount of their XOR (difference)
for index in range(m):
    diff = army[m]^army[index]
    if bin(diff).count("1") <= k:
        friends_count += 1

print(friends_count) 

