
# opposite sign between neighboring elements.
# maximum sum subsequence among all subsequences.

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # out put the maximum sum of the maximum size alternating subsequence
    res = []

    res.append(arr[0])
    for index, num in enumerate(arr):
        # same sign
        if num*res[-1] > 0:
            if num > res[-1]:
                res.pop()
                res.append(num)        
        else:
            res.append(num)

    print(sum(res))
