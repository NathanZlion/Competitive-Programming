


string1 = input()
string2 = input()

def areEquivalent(a: str, b: str) -> bool:
    if len(a)%2 or len(b)%2:
        return a == b

    if a == b:
        return True
    
    firstPossibility = areEquivalent(a[:len(a)//2],b[:len(b)//2]) and areEquivalent(a[len(a)//2:],b[len(b)//2:])
    if firstPossibility:
        return True

    secondPossibibilty = areEquivalent(a[len(a)//2:],b[:len(b)//2]) and areEquivalent(a[:len(a)//2],b[len(b)//2:])
    if secondPossibibilty:
        return True

    return False

print("YES" if areEquivalent(string1, string2) else "NO")