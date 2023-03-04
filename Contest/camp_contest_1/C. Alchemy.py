
n = int(input())

times = list(map(int, input().split()))

if n == 1:
    print(1,0)
else:
    left = 0
    right = n-1

    suma = times[left]
    sumb = times[right]

    counta = 1
    countb = 1
    while right > left+1:
        if suma > sumb:
            countb += 1
            right -= 1
            sumb += times[right]
        else:
            counta += 1
            left += 1
            suma += times[left]

    print(counta, countb)



