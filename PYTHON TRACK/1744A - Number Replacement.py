

t = int(input())

def solve():
    n = int(input())      # length of array
    a = list(map(int, input().split()))     # the array
    s = input()                       # the string of numbers

    freq = {}
    for i in range(len(a)):
        if not(a[i] in freq):
            freq[a[i]] = s[i]
        else:
            if not (freq[a[i]] == s[i]):
                print("NO")
                return
    print("YES")


for _ in range(t):
    solve()
