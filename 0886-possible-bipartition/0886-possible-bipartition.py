class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikeList = defaultdict(list)
        # 0 = unexplored
        # 1, -1 = the two groups

        for edge in dislikes:
            dislikeList[edge[0]].append(edge[1])
            dislikeList[edge[1]].append(edge[0])

        color = [0 for _ in range(n+1)]

        def dfs(index):
            if color[index] == 0:
                color[index] = -1
            
            for neighbor in dislikeList[index]:
                if color[neighbor] == 0:
                    color[neighbor] = color[index] * -1
                    if not dfs(neighbor):
                        return False

                elif color[neighbor] == color[index]:
                    return False
            
            return True


        for index in range(2, n+1):
            if color[index-1] == 0:
                if not dfs(index):
                    return False

        return True

