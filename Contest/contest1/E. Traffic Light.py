

def minimalSec(length,char,string):
    if char == 'g':
        return 0

    res = 0
    string *= 2

    curr_ptr = 0
    while curr_ptr < length:
        if string[curr_ptr] == char:
            ptr2 = curr_ptr
            while True:
                if (string[ptr2] == 'g'):
                    res = max(res, ptr2 - curr_ptr)
                    curr_ptr = ptr2 + 1
                    break
                ptr2 += 1
        else:
            curr_ptr += 1

    return res


t = int(input())
for i in range(t):
    [n, c] = input().split()
    n = int(n)
    s = input()
    print(minimalSec(n,c,s))


