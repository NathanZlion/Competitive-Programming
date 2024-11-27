class Solution:
    
    def shortestPath(self, start_node: int, end_node: int, adj_list: Dict[int, List[int]]) -> int:
        shortest_distance = { i : math.inf for i in range(len(adj_list))}
        
        shortest_distance[start_node] = 0
        _heap = [(0, start_node)]
        while _heap:
            curr_dist, curr_node = heappop(_heap)
            for next_node in adj_list[curr_node]:
                if shortest_distance[next_node] > curr_dist + 1:
                    shortest_distance[next_node] = curr_dist + 1
                    heappush(_heap, (curr_dist + 1, next_node))

        return shortest_distance[end_node]

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(n)}
        for i in range(n-1):
            adj_list[i].append(i+1)

        res = []
        for node_a, node_b in queries:
            adj_list[node_a].append(node_b)
            
            res.append(self.shortestPath(0, n-1, adj_list))
        
        return res
