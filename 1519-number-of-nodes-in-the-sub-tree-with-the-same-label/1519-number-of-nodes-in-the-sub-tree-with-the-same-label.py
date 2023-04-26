class Solution:

    def mergeLists(self, list1: List[int], list2: List[int]) -> None:
        for index in range(26):
            list1[index] += list2[index]


    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        # convert edges to adjecency list: undirected graph
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        # every node has atleast it self for the count
        res = [1 for _ in range(n)]
        visited = set()

        def dfs(node: int) -> List[int]:
            nonlocal res

            labelCount = [0 for _ in range(26)]

            for child in adjList[node]:
                if not child in visited:
                    visited.add(child)
                    self.mergeLists(labelCount, dfs(child))

            # now label count should have the sum of frequencies of each alphabet in all children

            nodeLabelIndex = ord(labels[node]) - 97
            res[node] += labelCount[nodeLabelIndex]
            labelCount[nodeLabelIndex] += 1

            return labelCount


        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)

        return res

