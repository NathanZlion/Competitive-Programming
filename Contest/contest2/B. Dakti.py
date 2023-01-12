
n = int(input())

def isNum(char):
    try:
        char = int(char)
        return True
    except:
        return False

def ordered(chorus):
    res = []
    for word in chorus:
        ordr = 0
        pureWord = ""
        for char in word:
            if isNum(char):
                ordr = int(char)
            else:
                pureWord += char

        res.append([ordr, pureWord])

    ret = []
    res.sort(key=lambda x: x[0])
    for wrd in res:
        ret.append(wrd[1])
    
    return " ".join(ret)


for i in range(n):
    chorus = input().split()
    print(ordered(chorus))
