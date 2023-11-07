length, reqSum = map(int, input().split())

def minNum(length: int, reqSum: int) -> int:
    if length == 0:
        return 0

    if length == 1:
        return reqSum

    for num in range(10):
        if (reqSum - num) <= (9*(length-1)) and (reqSum - num) >= 0:
            return (num*(10**(length-1))) + minNum(length-1, reqSum-num)

    return -1

def maxNum(length: int, reqSum: int) -> int:
    if length == 0:
        return 0

    if length == 1:
        return reqSum
    
    for num in range(9, -1, -1):
        if (reqSum - num) <= (9*(length-1)) and (reqSum - num) >= 0:
            return (num*(10**(length-1))) + maxNum(length-1, reqSum-num)

    return -1

minNumber = -1
maxNumber = -1

for num in range(1, 10):
    if (reqSum - num) <= (9*(length-1)) and (reqSum - num) >= 0:
        minNumber = (num*(10**(length-1))) + minNum(length-1, reqSum-num)
        break

for num in range(9, 0, -1):
    if (reqSum - num) <= (9*(length-1)) and (reqSum - num) >= 0:
        maxNumber = (num*(10**(length-1))) + maxNum(length-1, reqSum-num)
        break

print(minNumber, maxNumber)