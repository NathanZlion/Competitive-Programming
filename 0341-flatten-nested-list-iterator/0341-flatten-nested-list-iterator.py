# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ptr = 0
        self.nestedList = []
        for n in nestedList:
            self.nestedList.extend(NestedIterator._flatter(n))

        self.N = len(self.nestedList)

    def next(self) -> int:
        res = self.nestedList[self.ptr]
        self.ptr += 1
        return res

    def hasNext(self) -> bool:
        return self.ptr < self.N

    def _flatter(nestedList):
        if nestedList.isInteger():
            return [nestedList]

        res = []
        for n in nestedList.getList():
            res.extend(NestedIterator._flatter(n))

        return res


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())