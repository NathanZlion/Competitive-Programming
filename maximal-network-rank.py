class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        neighbor = defaultdict(set)
        for city1, city2 in roads:
            neighbor[city1].add(city2)
            neighbor[city2].add(city1)
        maxRank = 0
        for city1 in range(n):
            for city2 in range(city1+1, n):
                rank = len(neighbor[city1]) + len(neighbor[city2])
                if city1 in neighbor[city2]:
                    rank -= 1
                maxRank = max(rank, maxRank)
        
        return maxRank