class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        numberOfProvinces = 0
        explored = set()
        
        def explore(node):
            nonlocal explored
            nonlocal n

            if node in explored:
                return
            
            explored.add(node)
            
            for candidate in range(n):
                if isConnected[node][candidate] == 1:
                    explore(candidate)

            return


        for node in range(n):
            if node not in explored:
                numberOfProvinces += 1
                explore(node)
        
        return numberOfProvinces
