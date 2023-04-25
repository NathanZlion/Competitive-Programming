

n = int(input())

skills = list(map(int, input().split()))
skills.sort()

max_ = 0

l =0 
r = 0

while l < n and r < n:
    if skills[r] - skills[l] < 6:
        max_ = max(max_, r-l+1)
        r +=1
    else:
        l += 1

print(max_)