class TrieNode:
    def __init__(self):
        self.prefix_sum = 0
        self.children = {}

        
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.visited = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.visited:
            self.remove(key, self.visited[key])

        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
            curr.prefix_sum += val

        self.visited[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            
            curr = curr.children[char]
        
        return curr.prefix_sum
    
    def remove(self, key, val):
        curr = self.root
        for char in key:
            curr = curr.children[char]
            curr.prefix_sum -= val
