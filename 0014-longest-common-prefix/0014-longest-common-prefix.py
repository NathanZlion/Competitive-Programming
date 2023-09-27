class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordCount = 1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            else:
                curr.children[char].wordCount += 1

            curr = curr.children[char] 

    def insertWords(self, words: List[str]) -> None:
        for word in words:
            self.insertWord(word)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        trie.insertWords(strs)
        curr = trie.root
        N = len(strs)
        res = []

        while curr.children.__len__() == 1:
            nextChar = next(iter(curr.children))
            nextNode = curr.children[nextChar]

            if nextNode.wordCount != N:
                break

            res.append(nextChar)
            curr = nextNode

        return ''.join(res)