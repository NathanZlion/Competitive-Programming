# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
        # return a list of treenodes, that are roots of the possible binary trees.
        # I am thinking of using recursive functional call with remaining nodes as an argument
        """

        if n == 1:
            return [TreeNode()]
        
        if n == 0 or n == 2:
            return []
        
        res = []        
        for i in range(n):
            left_subtree = self.allPossibleFBT(i)
            right_subtree = self.allPossibleFBT(n-i-1)
            
            for left_child in left_subtree:
                for right_child in right_subtree:
                    res.append(TreeNode(0, left_child, right_child))


        return res
