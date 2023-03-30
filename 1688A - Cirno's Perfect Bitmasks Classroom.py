

t = int(input())

for _ in range(t):
    x = int(input())

    firstOn = float('inf')
    firstOff = float('inf')
    index = 0

    while True:
        if (x & (1<<index)) > 0:
            firstOn = index
            break
        
        index += 1

    index = 0
    while True:
        if ((x ^ (1<<index)) & (1<<index)) > 0:
            firstOff = index
            break

        index += 1


    if x == 2**firstOn:
        print(2**firstOn + 2**firstOff)
    else:
        print(2**firstOn)
