# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def doCount(self, node: Optional[TreeNode]) -> None:
        if not node:
            return

        self.count[node.val] += 1
        self.doCount(node.right)
        self.doCount(node.left)


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.count = defaultdict(int)

        self.doCount(root)
        max_ = max(self.count.values())
        
        res = []
        for k in self.count.keys():
            if self.count[k] == max_:
                res.append(k)

        return res
