q = int(input())

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 1

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.NUM_BITS = 30

    def insert(self, num: int) -> None:
        curr = self.root
        for i in range(self.NUM_BITS, -1, -1):
            bit = (num>>i)&1
            if not curr.children[bit]:
                curr.children[bit] = TrieNode()
            else:
                curr.children[bit].count += 1
            
            curr = curr.children[bit]

    def remove(self, num: int):
        curr = self.root
        for i in range(self.NUM_BITS, -1, -1):
            bit = (num>>i)&1
            if not curr.children[bit]:
                return

            curr.children[bit].count -= 1
            if curr.children[bit].count == 0:
                curr.children[bit] = None
                return

            curr = curr.children[bit]

    def findMaxXor(self, num: int) -> int:
        curr = self.root
        xor = 0
        for i in range(self.NUM_BITS, -1, -1):
            bit = (num>>i)&1

            if curr.children[1-bit]:
                xor |= (1<<i)
                curr = curr.children[1-bit]
            else:
                curr = curr.children[bit]
        
        return xor

trie = Trie()
trie.insert(0)

for _ in range(q):
    op, num = input().split()
    num = int(num)

    if op == '+':
        trie.insert(num)
    elif op == '-':
        trie.remove(num)
    else:
        print(trie.findMaxXor(num))

trie = None