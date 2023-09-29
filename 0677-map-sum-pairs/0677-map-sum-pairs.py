class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.visited = {}

    def insert(self, key: str, val: int) -> None:
        netVal = val
        if key in self.visited:
            netVal -= self.visited[key]

        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
            curr.count += netVal

        self.visited[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            
            curr = curr.children[char]
        
        return curr.count