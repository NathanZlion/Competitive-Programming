"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        explore all nodes and store in a hash map,
        for each node, add neighbors that are in the hashmap
        '''
        if not node:
            return None

        if not node.neighbors:
            return Node(node.val)
            

        map_ = {}
        
        stack = [node]
        
        while stack:
            currNode = stack.pop()
            map_[currNode] = Node(currNode.val)

            for neighbor in currNode.neighbors:
                if not neighbor in map_:
                    stack.append(neighbor)
        
        for oldNode, newNode in map_.items():
            for neighbor in oldNode.neighbors:
                newNode.neighbors.append(map_[neighbor])
        
        
        return map_[node]
            
            
            
            
            
            
            
            