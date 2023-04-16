class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # recursive algorithm.
        # change list to a adjecency list : Dict
        
        adjecencyList = defaultdict(list)
        maximumPathLength = 0

        for child, parent_ in enumerate(parent):            
            adjecencyList[parent_].append(child)

        def dfs(num):
            nonlocal maximumPathLength
            firstLongestPath = 0
            secondLongestPath = 0

            for child in adjecencyList[num]:
                childPathLength = dfs(child)

                if s[child] != s[num]:
                    if firstLongestPath < childPathLength:
                        secondLongestPath = firstLongestPath
                        firstLongestPath = childPathLength

                    elif secondLongestPath < childPathLength:
                        secondLongestPath = childPathLength

            maximumPathLength = max(maximumPathLength, firstLongestPath + 1 + secondLongestPath)


            return 1 + firstLongestPath

        maximumPathLength = max(dfs(0), maximumPathLength)


        return maximumPathLength


