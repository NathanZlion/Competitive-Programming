class Solution:

    def getMaxIndex(self,  currIndex, depthDce):
        for _ in range(depthDce):
            currIndex *= 2
            currIndex += 1

        return currIndex


    def kthGrammar(self, n: int, k: int) -> int:
        self.row = n
        self.column = k

        def backTrack(value, depth, index):
            if depth == self.row:
                return value

            # if maximum index found by going left is less than needed k go right
            if self.getMaxIndex(index*2, self.row - depth-1) < self.column-1:
                return backTrack(0, depth +1, index*2+1) if value == 1 else backTrack(1, depth +1, index*2+1)

            # go left if the index could be found in the left subtree
            return backTrack(1, depth +1, index*2) if value == 1 else backTrack(0, depth +1, index*2)

        return backTrack(0, 1, 0)
