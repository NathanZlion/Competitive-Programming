# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List, Dict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        graph: Dict[int, List] = self.binaryTreeToGraph(root)

        queue = deque([target.val])
        visited = set([target.val])

        # move k steps from the target
        for steps in range(k):
            if len(queue) == 0:
                return []

            for _ in range(len(queue)):
                curr = queue.popleft()

                for neighbor in graph[curr]:
                    if not neighbor in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        return list(queue)


    def binaryTreeToGraph(self, root: TreeNode) -> Dict[int, List]:
        graph : Dict[int, List] = {root.val: []}
        stack : List[TreeNode] = [root]

        while len(stack) > 0:
            curr = stack.pop()

            if curr.left:
                graph[curr.val].append(curr.left.val)
                graph[curr.left.val] = [curr.val]
                stack.append(curr.left)

            if curr.right:
                graph[curr.val].append(curr.right.val)
                graph[curr.right.val] = [curr.val]
                stack.append(curr.right)

        return graph
