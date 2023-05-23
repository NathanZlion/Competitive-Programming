
from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
    # for each prerequisites make the adjList and indegree dict

    adjList = defaultdict(list)
    indegree = defaultdict(int)

    for courseA, courseB in prerequisites:
        adjList[courseA].append(courseB)
        indegree[courseB] += 1
    
    queue = deque()
    for num in range(1, n+1):
        if indegree[num] == 0:
            queue.append(num)

    numberOfSemester = 0

    while len(queue) > 0:
        for _ in range(len(queue)):
            currCourse = queue.popleft()

            for neighbor in adjList[currCourse]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        numberOfSemester += 1

    for num in range(1, n+1):
        if indegree[num] != 0:
            return -1

    return numberOfSemester
