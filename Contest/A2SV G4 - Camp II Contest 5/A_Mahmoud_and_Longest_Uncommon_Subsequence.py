
# our task is to find the length of the longest uncommon subsequence
a, b = input(), input()

if a == b:
    print(-1)
else:
    print(max(len(a), len(b)))