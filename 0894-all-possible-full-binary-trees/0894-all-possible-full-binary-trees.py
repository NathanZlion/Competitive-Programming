# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
        # return a list of treenodes, that are roots of the possible binary trees.
        # I am thinking of using recursive functional call with remaining nodes as an argument
        """

        @cache
        def build_tree(remaining) -> List[Optional[TreeNode]]:
            if remaining == 1:
                return [TreeNode()]
            
            if remaining in [0, 2]:
                return []

            res = []
            
            for i in range(remaining):
                left_remaining = i
                right_remaining = remaining-i-1

                left_subtree = build_tree(left_remaining)
                right_subtree = build_tree(right_remaining)
                for left_child in left_subtree:
                    for right_child in right_subtree:
                        root = TreeNode(0, left_child, right_child)
                        res.append(root)

            return res

        return build_tree(n)
