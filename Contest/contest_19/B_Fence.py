

n, k = map(int, input().split())
height = list(map(int, input().split()))

res = 0

left = 0
running_sum = 0
min_sum = float("inf")

for right in range(n):
    running_sum += height[right]

    if right - left + 1 < k:
        continue

    if right - left + 1 > k:
        running_sum -= height[left]
        left += 1    

    if running_sum < min_sum:
        min_sum = running_sum
        res = left + 1

print(res if res > 0 else 1)
