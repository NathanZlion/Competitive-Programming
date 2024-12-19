# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        intToNodeMap = {}
        childSet = set()
        
        for parent, child, isLeft in descriptions:
            parentNode = intToNodeMap.get(parent, TreeNode(parent))
            childNode = intToNodeMap.get(child, TreeNode(child))
            intToNodeMap[parent] = parentNode
            intToNodeMap[child] = childNode
            
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
                
            childSet.add(child)
        
        for node in intToNodeMap:
            if node not in childSet:
                return intToNodeMap[node]
