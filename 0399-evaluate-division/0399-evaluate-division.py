
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build the graph from the equations and values
        adjList = defaultdict(list)
        existentKeys = set()
        valueDict = {}

        for (numerator, denominator), quotient in zip(equations, values):
            adjList[numerator].append(denominator)
            adjList[denominator].append(numerator)
            valueDict[(numerator, denominator)] = quotient
            valueDict[(denominator, numerator)] = 1.0 / quotient
            existentKeys.add(numerator)
            existentKeys.add(denominator)

        def solve( numerator: str, denominator: str) -> float:
            if numerator == denominator:
                return 1.000 if numerator in existentKeys else -1.000

            visited = set()
            visited.add(numerator)
            # deque => numerator, denominator, runningQuotient
            queue = deque()
            # traverse the neighbors of the numerator
            for deno in adjList[numerator]:
                if deno in visited: continue
                queue.append((deno, valueDict[(numerator, deno)]))
                visited.add(deno)

            while len(queue) > 0:
                numerator, runningProd = queue.popleft()
                if numerator == denominator:
                    return runningProd
                
                for deno in adjList[numerator]:
                    if deno in visited:
                        continue

                    queue.append((deno, runningProd * valueDict[(numerator,deno )]))
                    visited.add(deno)

            return -1

        # for every query compile your answer by calculating the answer
        answer = [0] * len(queries)

        for index, (num, deno) in enumerate(queries):
            answer[index] = solve(num, deno)

        return answer