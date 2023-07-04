from math import log2
from typing import List

t = int(input())


def is_sorted(lst: List[int], startPos: int = 0, endPos=None) -> bool:
    """This is a custom function I imlemented to check if a list is sorted."""
    if len(lst) == 0:
        return True

    endPos = endPos or len(lst)

    for index in range(startPos + 1, endPos):
        if lst[index] < lst[index - 1]:
            return False

    return True


def min_moves_to_beautify(arr: List[int], height: int, break_point: int) -> int:
    # basecase : at the leaves
    if height == 0:
        return 0

    child_dce = pow(2, (height - 2)) if height > 2 else 1

    left_break_point = break_point - child_dce
    right_break_point = break_point + child_dce

    # call funciton on the 2 children below
    left_moves = min_moves_to_beautify(arr, height - 1, left_break_point)
    right_moves = min_moves_to_beautify(arr, height - 1, right_break_point)

    span = pow(2, (height))

    start = break_point - (span // 2)
    end = break_point + (span // 2)

    if is_sorted(arr, start, end):
        return left_moves + right_moves

    else:
        # swap the 2 halves without slicing
        leftHalf = [arr[i] for i in range(start, break_point)]
        rightHalf = [arr[i] for i in range(break_point, end)]

        for i in range(start, break_point):
            arr[i] = rightHalf[i - start]

        for i in range(break_point, end):
            arr[i] = leftHalf[i - break_point]

        return left_moves + right_moves + 1x


for _ in range(t):
    m = int(input())
    n = int(log2(m))
    leaves = list(map(int, input().split()))

    min_moves = min_moves_to_beautify(
        arr=leaves, height=n, break_point=int(len(leaves) // 2)
    )

    print(min_moves if is_sorted(leaves) else -1)
