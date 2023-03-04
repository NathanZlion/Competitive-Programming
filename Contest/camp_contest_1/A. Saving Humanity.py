
test_cases = int(input())

for _ in range(test_cases):
    num_of_soliders,iterations = tuple(map(int, input().split()))
    inp = input()
    solider =list(map(int, [i for i in inp] ))


    newsolider = [life for life in solider]
    for _ in range(iterations):
        swapped = False

        if not newsolider[0]:
            if solider[1]:
                newsolider[0] = solider[1]
                swapped = True

        for i in range(1,num_of_soliders-1):
            if not newsolider[i]:
                if solider[i-1] ^ solider[i+1]:
                    newsolider[i] = 1
                    swapped = True

        if not newsolider[-1]:
            if solider[-2]:
                newsolider[-1]=1
                swapped = True

        solider = [life for life in newsolider]

        if not swapped: break

    print("".join(map(str, solider)))
