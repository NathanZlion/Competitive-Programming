class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.lockedBy = {}

        # convert to adjecency list
        adjList = defaultdict(list)

        for child, parent in enumerate(parent):
            adjList[parent].append(child)

        self.adjList = adjList


    def lock(self, num: int, user: int) -> bool:
        if num in self.lockedBy:
            return False
        
        self.lockedBy[num] = user
        return True


    def unlock(self, num: int, user: int) -> bool:
        if num in self.lockedBy:
            if self.lockedBy[num] == user:
                del self.lockedBy[num]
                return True
            
        return False

    def upgrade(self, num: int, user: int) -> bool:
        # the node is unlocked
        # has >= 1 locked descendants
        # has no locked ansestors

        if self.__hasNoLockedAncestors(num):
            lockedDescendants = self.__lockedDescendants(num)
            if lockedDescendants:
                self.lockedBy[num] = user
                for descendant in lockedDescendants:
                    self.lockedBy.pop(descendant, None)
            
                return True

        return False


    def __hasNoLockedAncestors(self, node: int) -> bool:
        while node >= 0:
            if node in self.lockedBy:
                return False
            
            node = self.parent[node]
        
        return True

    def __lockedDescendants(self, node:int) -> List[int]:
        lockedDescendants = []
        
        stack = [node]
        
        while stack:
            curr = stack.pop()
            
            for child in self.adjList[curr]:
                stack.append(child)

                if child in self.lockedBy:   # if we find a locked descendant
                    lockedDescendants.append(child)
        
        return lockedDescendants


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
