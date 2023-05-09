class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = {course: 0 for course in range(numCourses)}
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        for course, _indegree in indegree.items():
            if _indegree == 0:
                queue.append(course)
        
        
        while queue:
            course = queue.popleft()
            
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        for course, _indegree in indegree.items():
            if _indegree != 0:
                return False
        
        return True

        