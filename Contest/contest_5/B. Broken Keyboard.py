

t = int(input())

for _ in range(t):
    s = input()
    if len(s) == 1:
        print(s)

    elif len(s) == 2:
        if len(set(s)) == 2:
            print("".join(sorted(s)))
        else:
            print("")
        
    elif len(s) == 3:
        if len(set(s)) == 3:
            print("".join(sorted(s)))
        elif len(set(s)) == 2:
            se = set(s)
            for i in range(3):
                for j in range(i,3):
                    if s[i] == s[j]:
                        se.remove(s[i])
            print(se[0])
        else:
            print("")
    else:
        res = set()

        if s[0] != s[1]:
            res.add(s[0])

        if s[-1] != s[-2]:
            res.add(s[-1])

        for i in range(1,len(s)-1):
            if (s[i] != s[i-1] and s[i] != s[i+1]):
                res.add(s[i])

        print("".join(sorted(res, key=ord)))
