
from typing import List

n, minDifference = map(int, input().split())
arr: List[int] = list(map(int, input().split()))


def solve(start: int, end: int) -> List[int]:
    # base case : we are down to the last 2 competitors
    if end == start:
        return [start]

    # break down the array into 2 and merge them.
    mid = (start + end) // 2
    possibleLeftWinners = solve(start, mid)
    possibleRightWinners = solve(mid+1, end)

    return merge(possibleLeftWinners, possibleRightWinners)


def merge(left: List[int], right: List[int]) -> List[int]:
    leftMinimum = arr[left[0]]
    rightMinimum = arr[right[0]]

    leftPtr = 0
    rightPtr = 0

    # just have to win with the minimum
    while leftPtr < len(left) and arr[left[leftPtr]] + minDifference < rightMinimum:
        # exclude the left[leftPtr] coz it's too small
        leftPtr += 1

    while rightPtr < len(right) and arr[right[rightPtr]] + minDifference < leftMinimum:
        rightPtr += 1

    # making sure that the indices are sorted by the arr values at them
    # plus I wanted to do this in O(n) complexity so that it passes the runtime limit
    # so used a 2 pointer approach.
    merged = []
    while leftPtr < len(left) and rightPtr < len(right):
        if arr[left[leftPtr]] > arr[right[rightPtr]]:
            merged.append(right[rightPtr])
            rightPtr += 1
        else:
            merged.append(left[leftPtr])
            leftPtr += 1

    while leftPtr < len(left):
        merged.append(left[leftPtr])
        leftPtr += 1

    while rightPtr < len(right):
        merged.append(right[rightPtr])
        rightPtr += 1


    return merged


res = solve(0, len(arr)-1)
res.sort()
res = [i+1 for i in res]
print(*res)
