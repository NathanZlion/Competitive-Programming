
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    blue_ptr = -1
    red_ptr = n

    red_sum = 0
    blue_sum = 0

    # more blue count
    # more red sum
    possible = False

    while red_ptr > blue_ptr + 1:
        # if red_sum is not greater paint more red from the right
        if red_sum <= blue_sum:
            red_ptr -= 1
            red_sum += arr[red_ptr]
        
        # else if the blue count is not greater paint blue from left
        elif n - red_ptr >= blue_ptr+1:
            blue_ptr += 1
            blue_sum += arr[blue_ptr]

        # finally check the condition and update boolean possible
        if red_sum > blue_sum and blue_ptr+1 > n - red_ptr:
            possible = True
            break

    print("YES" if possible else "NO")


