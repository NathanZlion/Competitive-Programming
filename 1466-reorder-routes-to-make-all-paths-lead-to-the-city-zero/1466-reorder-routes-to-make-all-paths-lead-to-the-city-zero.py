class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = defaultdict(set)
        reverseAdjList = defaultdict(set)
        for src, dest in connections:
            adjList[src].add(dest)
            reverseAdjList[dest].add(src)

        numOfEdgesChanged = 0
        visited = set()
        visited.add(0)
        queue = deque()
        queue.append(0)
        
        while queue:
            currCity = queue.popleft()
            
            for neighbor in adjList[currCity]:
                if neighbor in visited:
                    continue

                numOfEdgesChanged += 1
                queue.append(neighbor)
                visited.add(neighbor)
            
            for neighbor in reverseAdjList[currCity]:
                if neighbor in visited:
                    continue
                
                queue.append(neighbor)
                visited.add(neighbor)

        return numOfEdgesChanged
