

def equalInst(name):
    freq ={}

    for letter in name:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    
    prev = 0
    flag = False
    for key in freq:
        if flag:
            if prev != freq[key]:
                return False
        prev = freq[key]
        flag = True
    
    return True


n = int(input())

members = list(input().split())
bad = set(input().split())

counter = 0
for i in range(n):
    if not(members[i] in bad):
        if equalInst(members[i]):
            counter += 1

print(counter)
            