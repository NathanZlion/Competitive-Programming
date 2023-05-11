class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        n = len(quiet)

        adjList = defaultdict(list)
        indegree = defaultdict(int)
        
        for rich, poor in richer:
            adjList[rich].append(poor)
            indegree[poor] += 1

        queue = deque()
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        answer = [i for i in range(n)]

        while queue:
            curr = queue.pop()
            
            for poor in adjList[curr]:
                if quiet[answer[curr]] < quiet[answer[poor]]:
                    answer[poor] = answer[curr]

                indegree[poor] -= 1
                if indegree[poor] == 0:
                    queue.append(poor)

        return answer
