
t = int(input())

def outlets_created(dividers):
    return sum(dividers) + 2

for _ in range(t):
    num_of_students, num_of_dividers = tuple(map(int, input().split()))
    outlets = list(map(int, input().split()))
    outlets.sort(reverse=True)
    for index in range(len(outlets)):
        outlets[index] -= 1

    # low => less than needed
    # high => more or equal than needed

    low = -1
    high = num_of_dividers + 1

    while high > low+1:
        mid = low + (high-low)//2
        if outlets_created(outlets[:mid]) < num_of_students:
            low = mid
        else:
            high = mid

    print(high if high <= num_of_dividers else -1)
