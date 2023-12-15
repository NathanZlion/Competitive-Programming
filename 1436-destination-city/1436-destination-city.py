class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegree = defaultdict(int)
        for from_, to_ in paths:
            outdegree[from_] += 1
            outdegree[to_] = outdegree[to_]
        
        for city in outdegree:
            if outdegree[city] == 0:
                return city
            