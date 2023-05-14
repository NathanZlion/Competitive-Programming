from typing import List
from collections import defaultdict, deque

from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int, m : int, edges : List[List[int]]) -> int:
        
        indegree = defaultdict(int)
        adjList = defaultdict(list)
        
        # process the edges
        for from_, to_ in edges:
            adjList[from_].append(to_)
            indegree[to_] += 1

        queue=deque()
        for node in range(1, n+1):
            if indegree[node] == 0:
                queue.append(node)
            
        answer = [0 for _ in range(n)]

        layer = 1

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                answer[curr-1] = layer

                for neighbor in adjList[curr]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            layer += 1
        
        return ' '.join(list(map(str,answer)))


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends