class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # from node 0 -> node n-1
        possiblePaths = []
        path = [0]
        
        def explore(currNode):
            nonlocal graph
            nonlocal path
            nonlocal possiblePaths
            
            if path[-1] == len(graph)-1:
                possiblePaths.append(path[:])

            for neighbor in graph[currNode]:
                path.append(neighbor)
                explore(neighbor)
                path.pop()
        
        
        explore(0)
        
        return possiblePaths
