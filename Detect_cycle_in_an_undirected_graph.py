
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
