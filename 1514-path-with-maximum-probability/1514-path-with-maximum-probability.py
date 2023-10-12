class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            adj_list[a].append((b, prob))
            adj_list[b].append((a, prob))
        
        min_prob = defaultdict(lambda : inf)
        min_prob[start_node] = -1
        heap = [(-1, start_node)]
        
        while heap:
            prob, node = heappop(heap)
            if node == end_node:
                break
                
            for next_node, edgeProb in adj_list[node]:
                if edgeProb * prob >= min_prob[next_node]:
                    continue

                min_prob[next_node] = edgeProb * prob
                heappush(heap, (min_prob[next_node], next_node))
        
        if min_prob[end_node] == inf:
            return 0.

        return -min_prob[end_node]
