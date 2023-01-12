

n = int(input())



words = []
for i in range(n):
    words.append(input())

res = ""

for i in range(len(words[0])):
    added = False
    key = ''
    for word in words:
        if (word[i] == '?'):
            continue
        elif not key:
            key = word[i]
        elif word[i] != key:
            res += '?'
            added = True
            break

    if not added:
        if key:
            res += key
        else:
            res += 'x'

print(res)
        
# 1
# ?a?b