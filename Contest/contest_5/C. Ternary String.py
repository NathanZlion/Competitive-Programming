

from collections import defaultdict

def check(d):
    return d["1"]>0 and d["2"]>0 and d["3"]>0

t = int(input())

for _ in range(t):
    min_ = 200001
    num = input()
    d = defaultdict(int)
    ptr1 = 0
    ptr2 = 0

    while ptr2 < len(num):
        if not check(d):
            d[num[ptr2]] += 1
            ptr2 += 1
            if check(d):
                min_ = min(ptr2-ptr1, min_)

        else:
            min_ = min(ptr2-ptr1, min_)
            d[num[ptr1]] -= 1
            ptr1 += 1

    if min_ == 200001:
        print(0)
    else:
        print(min_)
    

