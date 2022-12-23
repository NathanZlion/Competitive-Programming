if __name__ == '__main__':
    N = int(input())

    lst = []

    def run(inputCmd, lst):
        if inputCmd[0] == "print":
            print(lst)

        elif inputCmd[0] == "insert":
            lst.insert(int(inputCmd[1]), int(inputCmd[2]))

        elif inputCmd[0] == "remove":
            lst.remove(int(inputCmd[1]))

        elif inputCmd[0] == "append":
            lst.append(int(inputCmd[1]))

        elif inputCmd[0] == "sort":
            lst.sort()

        elif inputCmd[0] == "pop":
            lst.pop()

        elif inputCmd[0] == "reverse":
            lst = lst[::-1]
        return lst


    for _ in range(N):
        inputCmd = input().split()
        lst = run(inputCmd, lst)

