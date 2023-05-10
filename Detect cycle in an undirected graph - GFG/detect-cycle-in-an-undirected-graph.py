
from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:

		degree = {node: len(adj[node]) for node in range(V)}
		queue = deque()

		for node in range(V):
		    if degree[node] == 1:
		        queue.append(node)
		
		while queue:
		    curr = queue.popleft()
	        degree[curr] = 0

		    for neighbor in adj[curr]:
		        if degree[neighbor] > 0:
    		        degree[neighbor] -= 1
    
    		        if degree[neighbor] == 1:
    		            queue.append(neighbor)

        for node in range(V):
            if degree[node] != 0:
                return True

        return False


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends