
from heapq import heappop, heappush

n = int(input())
bob_ans = input()

#  smallest possible number without leading zeroes after shuffling the number
non_zeros = []
zeros_count = 0

while n:
    ones_place = n % 10
    if ones_place > 0:
        heappush(non_zeros, ones_place)
    else:
        zeros_count += 1
    n //= 10

res = 0
if zeros_count and non_zeros:
    res *= 10
    res += heappop(non_zeros)

res *= pow(10, zeros_count)

while non_zeros:
    res *= 10
    res += heappop(non_zeros)

print("OK" if str(res) == bob_ans else "WRONG_ANSWER")
