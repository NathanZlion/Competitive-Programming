
test_cases = int(input())

for _ in range(test_cases):
    num_of_rooms = int(input())
    evilness = list(map(int, input().split()))

    index = 0

    # go to the first non zero number
    while evilness[index] == 0:
        index += 1

    count = 0
    for i in range(index, num_of_rooms):
        if evilness[i] == 0:
            count += 1
        else:
            count += evilness[i]

    print(count)
