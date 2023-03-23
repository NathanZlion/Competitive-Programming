class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # build the graph from the edges given
        graph = {}
        for edge in edges:
            if not edge[0] in graph: graph[edge[0]] = []
            if not edge[1] in graph: graph[edge[1]] = []
            
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
    
        visited_nodes = set()

        # depth first traversal to get to the destination from the source node
        stack = [source]

        while len(stack) > 0:
            node = stack.pop()
            visited_nodes.add(node)
            if node == destination:
                return True
            
            for neighbour in graph[node]:
                if not neighbour in visited_nodes:
                    stack.append(neighbour)
            
        return False
