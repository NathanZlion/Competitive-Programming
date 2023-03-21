"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        traversedOrder = []
        while queue:
            length = len(queue)
            value = []
            for _ in range(length):
                root_val = queue.popleft()
                for child in root_val.children:
                    if child is not None:
                        queue.append(child)
                value.append(root_val.val)
            traversedOrder.append(value)
        
        return traversedOrder