
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        adjList = defaultdict(list)

        def explore(node: TreeNode) -> None:

            if node.left:
                adjList[node.val].append(node.left.val)
                adjList[node.left.val].append(node.val)
                explore(node.left)

            if node.right:
                adjList[node.val].append(node.right.val)
                adjList[node.right.val].append(node.val)
                explore(node.right)


        def findAtDepth(source: int, depth: int) -> List[int]:
            queue = deque()
            queue.append(source)
            visited = set()
            visited.add(source)

            for _ in range(depth):
                if not queue:                    
                    return []

                for __ in range(len(queue)):
                    curr = queue.popleft()

                    for neighbor in adjList[curr]:
                        if not neighbor in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

            return [ _ for _ in queue ]


        if root:
            explore(root)


        return findAtDepth(target.val, k)
