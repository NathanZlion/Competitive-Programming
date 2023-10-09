# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        minIndex, maxIndex = inf, -inf
        level = deque()
        level.append((0, root))

        while level:
            for _ in range(len(level)):
                index, node = level.popleft()
                minIndex = min(minIndex, index)
                maxIndex = max(maxIndex, index)

                if node.left:
                    level.append((index*2, node.left))

                if node.right:
                    level.append((index*2+1, node.right))

            maxWidth = max(maxWidth, maxIndex - minIndex + 1)
            minIndex, maxIndex = inf, -inf
            
        return maxWidth