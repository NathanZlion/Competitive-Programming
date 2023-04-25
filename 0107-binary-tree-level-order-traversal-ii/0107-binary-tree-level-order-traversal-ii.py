# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        res = []

        queue = deque()
        queue.append(root)
        
        while len(queue) > 0:
            layer = []
            # traversing one layer
            for _ in range(len(queue)):
                next = queue.popleft()
                layer.append(next.val)

                if next.left: queue.append(next.left)
                if next.right: queue.append(next.right)
                
            res.append(layer)


        res.reverse()
        return res

        