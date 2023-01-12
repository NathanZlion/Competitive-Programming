
nk = list(map(int, input().split()))
n, k = nk[0], nk[1]
theorem = list(map(int, input().split()))
awake = list(map(int, input().split()))


_sum = 0
for index in range(n):
    if awake[index]:
        _sum += theorem[index]

_max = 0
for index in range(k):
    if not awake[index]:
        _max += theorem[index]

ptr1 = 0
ptr2 = k

window_sum = _max
while ptr2 < n:
    window = window_sum
    if not awake[ptr1]:
        window_sum -= theorem[ptr1]

    if not awake[ptr2]:
        window_sum += theorem[ptr2]

    _max = max(_max, window_sum)
    ptr1 += 1
    ptr2 += 1


print(_sum + _max)