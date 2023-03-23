class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # construct the undirected graph from the edges
        # start at any node and build candidates

        graph = defaultdict(set)

        # constructing the graph
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

            if len(graph[edge[0]]) > 1:
                return edge[0]
            if len(graph[edge[1]]) > 1:
                return edge[1]