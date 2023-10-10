# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        repr_id = {}
        count = defaultdict(int)

        def traverse(node: Optional[TreeNode]) -> List[int | None]:
            if not node:
                return 0

            representation = (traverse(node.left), node.val, traverse(node.right))
            if representation not in repr_id:
                repr_id[representation] = len(repr_id) + 1
            
            count[representation] += 1
            if count[representation] == 2:
                res.append(node)

            return repr_id[representation]


        traverse(root)
        return res