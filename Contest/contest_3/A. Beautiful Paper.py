


t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    printed = False

    if a[0] == b[0]:
        if (a[1] + b[1] == a[0]):
            print("YES")
            printed = True
       
    if a[0] == b[1]:
        if a[1] + b[0] == a[0]:
            print("YES")
            printed = True
        
    
    if a[1] == b[0]:
        if a[0] + b[1] == a[1]:
            print("YES")
            printed = True
        
    
    if a[1] == b[1]:
        if a[0] + b[0] ==a[1]:
            print("YES")
            printed = True
       

    if not printed:print("NO")
