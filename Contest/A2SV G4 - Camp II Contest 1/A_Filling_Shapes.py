
from math import pow


n = int(input())

if n % 2:
    print(0)
else:
    print(int(pow(2, n//2)))