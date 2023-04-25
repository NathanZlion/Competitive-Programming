

t = int(input())

def trailingZeros(num):
    ctr = 0
    while not num & 1:
        ctr += 1
        num >>= 1
    return ctr


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # try every possibility
    num_of_shifts = 0
    shifted = []

    for index in range(n):
        num = arr[index]
        while not num & 1:
            num_of_shifts += 1
            num >>= 1
        shifted.append(num)
        
    
    max_sum = 0
    for index in range(n):
        temp = shifted[index]
        shifted[index] = arr[index] << (num_of_shifts - trailingZeros(arr[index]))
        max_sum = max(sum(shifted), max_sum)
        shifted[index] = temp
    
    print(max_sum)



