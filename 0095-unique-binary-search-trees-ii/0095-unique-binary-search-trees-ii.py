# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # from 1 to n:  structurally different
        
        def backtrack(left : int, right: int) -> Optional[List[TreeNode]]:
            roots : List[TreeNode] = []

            for root_node_val in range(left, right):
                left_nodes = backtrack(left, root_node_val)
                right_nodes = backtrack(root_node_val +1, right)

                for left_node in left_nodes:
                    for right_node in right_nodes:
                        roots.append(TreeNode(root_node_val, left_node, right_node))

            return roots if len(roots) > 0 else [None]

        return backtrack(left = 1, right = n + 1)