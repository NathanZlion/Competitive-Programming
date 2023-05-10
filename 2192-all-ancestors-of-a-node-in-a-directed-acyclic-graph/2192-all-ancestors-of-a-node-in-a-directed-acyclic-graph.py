class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # process the edges
        # hold an adjList, indegree
        
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        
        for _from, _to in edges:
            indegree[_to] += 1
            adjList[_from].append(_to)
        
        queue = deque()
        for index in range(n):
            # start from 0 indegree nodes
            if indegree[index] == 0:
                queue.append(index)


        answer = [set() for _ in range(n)]
        while queue:
            curr = queue.pop()
            
            for neighbor in adjList[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
                
                answer[neighbor].add(curr)
                for ancestor in answer[curr]:
                    answer[neighbor].add(ancestor)
        
        for index, set_ in enumerate(answer):
            answer[index] = sorted(list(set_))
        
        
        return answer
            
        