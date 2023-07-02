from typing import List

t = int(input())


def solve(arr, builtList: List[int] = [], runningSum: int = 0, visited: set = set()):
    if len(builtList) == len(arr):
        return builtList

    for index in range(len(arr)):
        if (arr[index] != runningSum) and (index not in visited):
            builtList.append(arr[index])
            visited.add(index)
            res = solve(arr, builtList, runningSum + arr[index], visited)
            if res != None:
                return res
            builtList.pop()
            visited.remove(index)

    return None


for _ in range(t):
    # 2 <= n <= 50
    n = int(input())
    arr = list(map(int, input().split()))
    res = solve(arr, [], 0, set())

    if res != None:
        print("YES")
        print(*res)
    else:
        print("NO")
