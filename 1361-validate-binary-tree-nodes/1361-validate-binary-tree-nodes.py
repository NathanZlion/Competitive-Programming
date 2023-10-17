class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegreeCount = defaultdict(int)
        
        for node, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                indegreeCount[left] += 1

            if right != -1:
                indegreeCount[right] += 1

        rootNode = -1
        for node in range(n):
            if indegreeCount[node] == 0:
                rootNode = node
                break

        if rootNode == -1:
            return False

        visited = [False for _ in range(n)]
        queue = deque()
        queue.append(rootNode)
        while queue:
            curr = queue.popleft()
            if visited[curr]:
                return False

            visited[curr] = True
            
            if leftChild[curr] != -1:
                queue.append(leftChild[curr])
            
            if rightChild[curr] != -1:
                queue.append(rightChild[curr])

        return all(visited)