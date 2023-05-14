class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adjList = defaultdict(list)
        indegree = defaultdict(int)

        for coursea, courseb in prerequisites:
            adjList[coursea].append(courseb)
            indegree[courseb] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        allPrerequisites = [set() for _ in range(numCourses)]
        while queue:
            curr = queue.pop()

            for neighbor in adjList[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

                allPrerequisites[neighbor].add(curr)
                allPrerequisites[neighbor] = allPrerequisites[neighbor].union(allPrerequisites[curr])
        
        return [a in allPrerequisites[b] for a, b in queries]
