class Solution:
    def calcEquation( self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for val, (numerator, denominator) in zip(values, equations):
            adjList[numerator].append((denominator, val))
            adjList[denominator].append((numerator, 1/val))

        def dfs(start: str, end: str, visited: set) -> float:
            if start in visited or start not in adjList:
                return -1

            visited.add(start)

            if end == start:
                return 1

            for deno, val in adjList[start]:
                quotient = dfs(deno, end, visited)
                if quotient != -1:
                    return val * quotient

            return -1

        res = []
        for numerator, denominator in queries:
            res.append(dfs(numerator, denominator, set()))

        return res