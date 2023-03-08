# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        
        def helper(root, row, col):
            if not root:
                return
            
            res[root] =  [row, col]

            helper(root.left, row +1, col-1)
            helper(root.right, row+1, col+1)
        
        helper(root, 0, 0)


        colMap = defaultdict(list)

        for node in res.keys():
            colMap[res[node][1]].append(node)
        
        for column in colMap.keys():
            colMap[column].sort(key = lambda x: (res[x][0], x.val) )
        
        colMapkeys = sorted(colMap)
        
        ans = []

        for column in colMapkeys:
            col = []
            for node in colMap[column]:
                col.append(node.val)
            
            ans.append(col)

        return ans
        