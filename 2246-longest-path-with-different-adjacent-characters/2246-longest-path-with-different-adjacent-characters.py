class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # recursive algorithm.
        # change list to a adjecency list : Dict
                
        if len(parent) < 2:
            return len(parent)

        
        adjecencyList = defaultdict(list)
        maximumPathLength = 0

        for child, parent_ in enumerate(parent):            
            adjecencyList[parent_].append(child)

        def dfs(num):
            nonlocal maximumPathLength
            count = 1
            paths = []

            for child in adjecencyList[num]:
                childPathLength = dfs(child)

                if s[child] != s[num]:
                    paths.append(childPathLength)

            if paths:
                currMax = 1

                if len(paths) == 1:
                    currMax += paths[-1]

                elif len(paths) > 1:
                    paths.sort()
                    currMax += paths[-1] + paths[-2]

                maximumPathLength = max(maximumPathLength, currMax)

            return 1 + paths.pop() if paths else 1


        maximumPathLength = max(dfs(0), maximumPathLength)
        return maximumPathLength


