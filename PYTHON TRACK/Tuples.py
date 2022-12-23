if __name__ == '__main__':
    n = int(input())
    nums = tuple(map(int, input().split()))

    print(hash(nums))
