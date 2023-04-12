class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.child = defaultdict(list)
        self.isAlive = defaultdict(lambda : True)
        self.inheritance = []

    def birth(self, parentName: str, childName: str) -> None:
        self.child[parentName].append(childName)

    def death(self, name: str) -> None:
        self.isAlive[name] = False

    def getInheritanceOrder(self) -> List[str]:
        self.inheritance.clear()
        self.dfs(self.kingName)
        return self.inheritance
    
    def dfs(self, name: str) -> None:
        if self.isAlive[name]:
            self.inheritance.append(name)

        for childName in self.child[name]:
            self.dfs(childName)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()