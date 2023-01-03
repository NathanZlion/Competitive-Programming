n = int(input())
 
 
hash_val = {
    'S' : 0.1,
    'M' : 1,
    'L' : 10
}
 
 
def size(a):
    val_a = hash_val[a[-1]]
 
    if len(a) == 1:
        return val_a
    return pow(val_a, len(a))
 
 
def compare(a, b):
    if (a == b):
        return '='
 
    elif (a > b):
        return '>'
 
    return '<'
 
 
for i in range(n):
    ab = input().split()
    a = ab[0]
    b = ab[1]
    print(compare(size(a), size(b)))
