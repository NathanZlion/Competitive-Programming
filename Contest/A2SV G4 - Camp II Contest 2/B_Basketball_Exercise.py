numOfStudents = int(input())
arr = [list(map(int, input().split())), list(map(int, input().split()))]
arr[0].append(0)
arr[1].append(0)

# bottom up dp
for row in range(2):
    for index in range(numOfStudents - 2, -1, -1):
        maxNextHeight= 0
        if index+2 < numOfStudents:
            maxNextHeight = max(maxNextHeight, arr[1-row][index+1])

        if index+1< numOfStudents:
            maxNextHeight = max(maxNextHeight, arr[1-row][index+1])

        arr[row][index] += maxNextHeight
        arr[row][index] = max(arr[row][index], arr[row][index+1])


print(max(arr[0][0], arr[0][1]))