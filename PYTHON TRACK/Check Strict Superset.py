
lstA = input().split()

n = int(input())

def check(lst):
    for i in lst:
        if not(i in lstA):
            return False

    for i in lstA:
        if not(i in lst):
            return True

    return False

res = "True"
for i in range(n):
    lstB = input().split()

    if not check(lstB):
        res = "False"

print(res)


