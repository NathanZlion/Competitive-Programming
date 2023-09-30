class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]

    def checkAndInsert(self, word: str) -> bool:
        curr = self.root
        
        for i in range(len(word)-1):
            char = word[i]
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        self.insert(word)
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()
        res = ""
        for word in words:
            if trie.checkAndInsert(word):
                if len(word) > len(res):
                    res = word
            
        return res
