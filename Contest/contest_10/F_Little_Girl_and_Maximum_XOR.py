
l, r = map(int, input().split())

n = 0
# iterate through all bits
while 2**n <= r:
    # if they have same bit at n in from left
    if ((l^r)&(1<<n)) == 0:
        # both have 1
        if (l & 1<<n) > 0:
            temp = r - (2**n)
            if temp >= l:
                r = temp

        else:
            temp = l + (2**n)
            if temp <= r:
                l = temp

    n += 1

print(l^r)

