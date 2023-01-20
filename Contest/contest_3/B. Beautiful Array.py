

n = int(input())

arr = list(map(int, input().split()))

negatives = []
positives = []
zeros = []


for num in arr:
    if num > 0:
        positives.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        negatives.append(num)

if len(positives) == 0:
    positives.append(negatives.pop())
    positives.append(negatives.pop())

if not (len(negatives) % 2):
    zeros.append(negatives.pop())


print(len(negatives),end=" ")
for neg in negatives:
    print(neg, end = " ")
print()

print(len(positives),end=" ")

for pos in positives:
    print(pos, end = " ")
print()

print(len(zeros),end=" ")

for zero in zeros:
    print(zero, end = " ")

