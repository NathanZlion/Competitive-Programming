class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # keep track of count of edges a node has
        # keep track if there is a connection between a node
        
        connections = defaultdict(set)
        
        for edge in roads:
            connections[edge[0]].add(edge[1])
            connections[edge[1]].add(edge[0])
        
        maxRank = 0
        for node1 in connections:
            for node2 in connections:
                if node1 == node2:
                    continue
                
                currRank = 0
                if node2 in connections[node1]:
                    currRank -= 1
                currRank += len(connections[node1])
                currRank += len(connections[node2])
                
                maxRank = max(maxRank, currRank)
            
        return maxRank
                                            
                                            
                    
            