

x = input()

lst = []

for (index, digit) in enumerate(x):
    digit = int(digit)
    if digit == 9:
        if index == 0:
            lst.append(digit)
        else:
            lst.append(9-digit)

    elif digit == 0:
        if index == 0:
            lst.append(9)
        else:
            lst.append(0)
    elif digit > 4:
        lst.append(9-digit)
    else:
        lst.append(digit)


length = len(x)

res = 0

for index, digit in enumerate(lst):
    res += 10**(length - index -1) * digit

print(res)
