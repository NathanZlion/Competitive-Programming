

# minimum number of swaps to make parity correct
# count out of place odds
# count out of place evens

# if different print -1
# is same print count of either one of the,

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    evens_out_of_place = 0
    odds_out_of_place = 0

    for index, num in enumerate(arr):
        # odd index
        if index % 2:
            if not num % 2:
                odds_out_of_place += 1
        
        else:
            if num % 2:
                evens_out_of_place += 1
    
    if evens_out_of_place == odds_out_of_place:
        print(odds_out_of_place)
    
    else:
        print(-1)


