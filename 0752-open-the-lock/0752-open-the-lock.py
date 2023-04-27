class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        setOfDeadends = set()

        for deadend in deadends:
            setOfDeadends.add(tuple(map(int, tuple(deadend))))

        explored : set[tuple[int]] = set()
        target = tuple([int(num) for num in target])

        moves = [[ 1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], \
                      [-1, 0, 0, 0], [0,-1, 0, 0], [0, 0,-1, 0], [0, 0, 0,-1]]

        def addTwoLists(list1: List[int], list2: List[int]) -> None:
            for index in range(4):
                list1[index] += list2[index]
                list1[index]%=10

        def subtractTwoLists(list1: List[int], list2: List[int]) -> None:
            for index in range(4):
                list1[index] -= list2[index]
                list1[index]%=10

        queue = deque()
        queue.append([0, 0, 0, 0])
        currentDepth = 0
        explored.add((0,0,0,0))

        while len(queue) > 0:
            for _ in range(len(queue)):
                currLock = queue.popleft()
                currLockTuple = tuple(currLock)

                if currLockTuple == target:
                    return currentDepth

                if currLockTuple in setOfDeadends:  # no further expanding so don't add to the queue
                    continue

                for move in moves:
                    addTwoLists(currLock, move)

                    if tuple(currLock) not in explored:
                        explored.add(tuple(currLock))
                        queue.append(currLock.copy())

                    subtractTwoLists(currLock, move)

            currentDepth += 1

        return -1

        