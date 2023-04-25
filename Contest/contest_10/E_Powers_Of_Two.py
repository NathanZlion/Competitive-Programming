n,k=map(int, input().split())

ans = []

def backTrack(num):
    if len(ans) >= k:
        return num == 0

    if num == 0:
        return len(ans) == k

    n = 0
    while 2**n <= num:
        power = 2**n 
        num -= power
        ans.append(power)
        if backTrack(num):
            return True
        ans.pop()
        num += power

        n += 1

    return False


if backTrack(n):
    print("YES")
    print(*ans)
else:
    print("NO")