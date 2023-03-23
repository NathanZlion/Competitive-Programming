class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # construct the undirected graph from the edges
        # start at any node and build candidates

        graph = defaultdict(set)
        all_nodes = set()

        # constructing the graph
        for edge in edges:
            all_nodes.add(edge[0])
            all_nodes.add(edge[1])
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        # for each node check if it has all the nodes except self...
        for node in all_nodes:
            all_nodes.remove(node)
            if graph[node] == all_nodes:
                return node
            all_nodes.add(node)
