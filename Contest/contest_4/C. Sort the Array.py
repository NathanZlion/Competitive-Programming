

n = int(input())
arr = list(map(int, input().split()))


def isSorted(lst):
    arrSorted = sorted(lst)
    for index in range(len(lst)):
        if lst[index] != arrSorted[index]:
            return False

    return True


right = n-1
while right > 0:
    if arr[right-1] <= arr[right]:
        right -= 1
    else:
        break

if right != 0:
    left = 0
    while left < right:
        if arr[left] <= arr[left+1]:
            left += 1
        else:
            break

    l, r = left, right

    # swap in place
    while r > l:
        arr[r], arr[l] = arr[l], arr[r]
        r -= 1
        l += 1

    if isSorted(arr):
        print("yes")
        print(f'{left+1} {right+1}')
    else:
        print("no")

else:
    print("yes")
    print("1 1")


