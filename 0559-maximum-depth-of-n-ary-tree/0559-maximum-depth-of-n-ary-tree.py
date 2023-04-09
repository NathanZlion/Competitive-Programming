"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def maxDepth(self, root: 'Node') -> int:
        
        if not root:return 0

        # iterative bfs
        queue = deque()
        queue.append(root)
        
        currDepth = 0

        while len(queue) > 0:
            currDepth += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                for neighbor in curr.children:
                    queue.append(neighbor)

        return currDepth
                
                
            
        
    
