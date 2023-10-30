# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)

        def traverse(node: TreeNode | None, parent_deleted: bool) -> None:
            if not node:
                return
        
            to_be_deleted = node.val in to_delete
            if parent_deleted and not to_be_deleted:
                res.append(node)
                
            traverse(node.left, to_be_deleted)
            traverse(node.right, to_be_deleted)

            if node.left and node.left.val in to_delete:
                node.left = None
            
            if node.right and node.right.val in to_delete:
                node.right = None

        traverse(root, True)
        return res