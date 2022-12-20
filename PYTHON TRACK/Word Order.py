
n = int(input())

freq = {}
for i in range(n):
    word = input()
    if word in freq:
        freq[word] +=1
    else:
        freq[word] = 1

print(len(freq))

for key in freq:
    print(freq[key], end=" ")
