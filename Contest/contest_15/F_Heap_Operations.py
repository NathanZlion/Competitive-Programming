

from heapq import heappop, heappush

num_records_left = int(input())

operations = []
# insert x
# removeMin
# getMin x

heap = []

# n lines of records
for _ in range(num_records_left):
    operation = input().split()

    # removeMin
    if len(operation) == 1:
        if not heap:
            heappush(heap, 1_000_000_000)
            operations.append("insert 0")

        heappop(heap)
        operations.append("removeMin")

    else:
        # insert: insert no questions asked
        if operation[0] == "insert":
            heappush(heap, int(operation[1]))
            operations.append("insert "+ operation[1])

        # getMin
        else:
            # remove less numbers
            while heap and heap[0] < int(operation[1]):
                heappop(heap)
                operations.append("removeMin")

            if not heap or (heap and heap[0] != int(operation[1])):
                heappush(heap, int(operation[1]))
                operations.append("insert "+ operation[1])

            operations.append("getMin "+ (operation[1]))


print(len(operations))

for operation in operations:
    print(operation)

