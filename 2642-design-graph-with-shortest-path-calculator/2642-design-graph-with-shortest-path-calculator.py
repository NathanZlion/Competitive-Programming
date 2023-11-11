class Graph:

    def __init__(self, n, edges):
        self.adj_matrix = [[inf] * n for _ in range(n)]
        for from_node, to_node, cost in edges:
            self.adj_matrix[from_node][to_node] = cost
        for i in range(n):
            self.adj_matrix[i][i] = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.adj_matrix[j][k] = min(self.adj_matrix[j][k],
                                                self.adj_matrix[j][i] + 
                                                self.adj_matrix[i][k])

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        n = len(self.adj_matrix)
        for i in range(n):
            for j in range(n):
                self.adj_matrix[i][j] = min(self.adj_matrix[i][j],
                                            self.adj_matrix[i][from_node] + 
                                            self.adj_matrix[to_node][j] +
                                            cost)

    def shortestPath(self, node1, node2):
        if self.adj_matrix[node1][node2] == inf: return -1
        return self.adj_matrix[node1][node2]