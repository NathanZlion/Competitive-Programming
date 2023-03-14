# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def successor(self, node: TreeNode) -> int:
        while node.left:
            node = node.left
        
        return node.val

        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:        
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        elif not (root.right or root.left):
            return None

        elif root.right:
            successor = self.successor(root.right)
            root.val = successor
            root.right = self.deleteNode(root.right, successor)

        else:
            root = root.left


        return root        
