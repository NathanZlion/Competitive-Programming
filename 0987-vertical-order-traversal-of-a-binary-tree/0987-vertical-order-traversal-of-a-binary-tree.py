# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeRowColMap = {}

        def traverse(root, row, col):
            if not root:
                return

            nodeRowColMap[root] =  [row, col]
            traverse(root.left, row +1, col-1)
            traverse(root.right, row+1, col+1)

        traverse(root, 0, 0)


        colMap = defaultdict(list)

        for node in nodeRowColMap.keys():
            colMap[nodeRowColMap[node][1]].append(node)

        for column in colMap.keys():
            colMap[column].sort(key = lambda x: (nodeRowColMap[x][0], x.val) )

        verticalTraversal = []

        for column in sorted(colMap):
            col = []
            for node in colMap[column]:
                col.append(node.val)

            verticalTraversal.append(col)

        return verticalTraversal
