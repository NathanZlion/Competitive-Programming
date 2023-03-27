
t = int(input())

for _ in range(t):
    number_of_monsters = int(input())
    health = list(map(int, input().split()))

    # Things you can do :
    # choose exactly two alive monsters and decrease their health by 1
    # choose a single monster and kill it.

    health.sort()

    number_of_casts = 0
    left_ptr = 0
    right_ptr = number_of_monsters-1

    while right_ptr >= left_ptr:
        while left_ptr < number_of_monsters and health[left_ptr] == 0:
            left_ptr += 1

        if left_ptr >= number_of_monsters:
            break

        if health[left_ptr] == 1 and left_ptr < number_of_monsters-1:
            health[left_ptr] -= 1
            health[left_ptr+1] -= 1
            number_of_casts += 1
        
        else:
            right_ptr -= 1
            number_of_casts += 1

    print(number_of_casts)