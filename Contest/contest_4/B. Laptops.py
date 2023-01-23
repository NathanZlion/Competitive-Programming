
from collections import defaultdict


n = int(input())

price = []
quality = []

for _ in range(n):
    [a, b] = list(map(int, input().split()))
    price.append(a)
    quality.append(b)


priceToQuality = defaultdict()
# let me use bubble sort to sort the price
for index in range(n):
    priceToQuality[price[index]] = quality[index]


price.sort()

alexo = False

for index in range(n-1):
    if priceToQuality[price[index]] > priceToQuality[price[index+1]]:
        alexo = True
        break

if alexo:
    print("Happy Alex")
else:
    print("Poor Alex")


