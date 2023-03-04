

n = int(input())
names = list(map(str, input().split()))

queries = int(input())

for _ in range(queries):
    name = input()

    left = -1
    right = n
    while right > left +1:
        mid = left + (right-left)//2
        if names[mid] < name:
            left = mid
        else:
            right = mid
    
    print(left+1)


