class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            else:
                curr.children[char].count += 1
            curr = curr.children[char]
    
    def findScore(self, word: str) -> int:
        curr = self.root
        score = 0

        for char in word:
            curr = curr.children[char]
            score += curr.count
        
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return [trie.findScore(word) for word in words]