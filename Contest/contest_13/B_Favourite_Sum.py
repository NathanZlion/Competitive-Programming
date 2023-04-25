

# arr, x

t = int(input())

for _ in range(t):
    n, x = map(int, input().split()) # the number of favorite integers, X
    favorite_numbers = list(map(int, input().split()))

    # sum 1 to X
    # subtract 2* favorite numbers in the range [1, x]
    total_sum = ((x)*(x+1))//2

    for num in favorite_numbers:
        if 1 <= num <= x:
            total_sum -= (2*num)
    
    print(total_sum)



