class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # representation:
            # -1: undiscovered
            #  0: beginning
            #  1: discovered

        # build the graph
        adjList = defaultdict(list)

        for edge in edges:
            adjList[edge[0]].append(edge[1])

        nodeState = [-1 for _ in range(n)]

        # traverse each node holding a list of length n
        stack = []

        for index in range(n):
            if nodeState[index] == -1:
                nodeState[index] = 0
                for neighbor in adjList[index]:
                    stack.append(neighbor)


            while stack:
                currIndex = stack.pop()

                if nodeState[currIndex] == 1:
                    continue

                nodeState[currIndex] = 1
                
                for neighbor in adjList[currIndex]:
                    stack.append(neighbor)

        res = []
        for index in range(n):
            if nodeState[index] == 0:
                res.append(index)

        return res
