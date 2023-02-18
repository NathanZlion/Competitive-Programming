

t = int(input())

for _ in range(t):
    n,m,k = tuple(map(int, input().split()))

    a = input()
    b = input()

    a_moves = 0
    b_moves = 0
    c = []

    a_lst = [char for char in a]
    b_lst = [char for char in b]

    while a_lst and b_lst:
        if a_moves == k:
            c.append(b_lst.pop(b_lst.index(min(b_lst))))
            b_moves += 1
            a_moves = 0
        elif b_moves == k:
            c.append(a_lst.pop(a_lst.index(min(a_lst))))
            a_moves += 1
            b_moves = 0
        
        else:
            a_min = min(a_lst)
            b_min = min(b_lst)

            if (a_min <= b_min):
                c.append(a_lst.pop(a_lst.index(a_min)))
                a_moves += 1
                b_moves = 0
            else:
                c.append(b_lst.pop(b_lst.index(b_min)))
                b_moves += 1
                a_moves = 0


    print("".join(c))

