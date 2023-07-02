

letter = input()

upper = [0]*len(letter)
lower = [0]*len(letter)

# right most uppercase
right = -1

# left most lowercase
left = len(letter)

for index, char in enumerate(letter):
    if char.islower():
        left = min(left, index)
        lower[index] = 1
    else:
        right = index
        upper[index] = 1

# prefix sum of lowercases
for index in range(1, len(letter)):
    lower[index] += lower[index-1]

# 'suffix sum' of uppercase count
for index in reversed(range(-1, len(letter)-1)):
    upper[index] += upper[index+1]

poss1 = lower[right] if right != -1 else 0
poss2 = upper[left] if left != len(letter) else 0

print(min(poss1, poss2))


