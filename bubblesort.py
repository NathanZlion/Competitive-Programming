def countSwaps(a):
    notSorted = True
    numSwaps = 0
    while notSorted:
        notSorted = False  
        for i in range(len(a) -1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                numSwaps += 1
                notSorted = True
    print(f'Array is sorted in {numSwaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
