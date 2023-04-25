

# generate the prime numbers upto n+1 inclusive
# prime divisor

n = int(input())

colors = [1 for _ in range(n)]
def generate_primes(end):
    isprime = [True for _ in range(end+1)]
    isprime[0] = False
    isprime[1] = False

    for index in range(end+1):
        num = index
        if not isprime[index]:
            continue

        for i in range(2, int(num**0.5)+1):
            if index%i == 0:
                isprime[num] = False
                break

        if isprime[num]:
            temp = num
            temp += num
            while temp < end+1:
                isprime[temp] = False
                temp += index

    return isprime

primes = generate_primes(n+1)

for i in range(2, n+1):
    if primes[i]:
        ctr = 1
        temp = i

        while temp < n+2:
            colors[temp-2] = ctr
            ctr += 1
            temp += i
        

print(max(colors))
print(colors)







