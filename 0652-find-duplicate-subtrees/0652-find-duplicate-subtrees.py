# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = {}
        res = []
        
        def traverse(node: Optional[TreeNode]) -> List[int | None]:
            if not node:
                return [None]

            representation = [node.val]
            representation.extend(traverse(node.left))
            representation.extend(traverse(node.right))
            
            count[str(representation)] = count.get(str(representation), 0) + 1
            if count.get(str(representation), 0) == 2:
                res.append(node)

            return representation

        traverse(root)
        return res