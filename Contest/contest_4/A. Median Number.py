

t = int(input())

for _ in range(t):
    lst = list(map(int, input().split()))
    lst.pop(lst.index(min(lst)))
    lst.pop(lst.index(max(lst)))
    print(lst.pop())
