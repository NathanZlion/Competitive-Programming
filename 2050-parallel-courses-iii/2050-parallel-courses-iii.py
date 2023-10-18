class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # first build the topological sorting of the courses
        # hold a separate dictionary of the the min month

        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for prev_course, next_course in relations:
            indegree[next_course] += 1
            graph[prev_course].append(next_course)

        stack = []
        minTime = defaultdict(lambda: 0)
        for i in range(1, n+1):
            if indegree[i] == 0:
                stack.append(i)
                minTime[i] = time[i-1]

        while stack:
            curr_node = stack.pop()

            for child in graph[curr_node]:
                minTime[child] = max(minTime[child], time[child-1] + minTime[curr_node])
                indegree[child] -= 1

                if indegree[child] == 0:
                    stack.append(child)

        return max(minTime.values())