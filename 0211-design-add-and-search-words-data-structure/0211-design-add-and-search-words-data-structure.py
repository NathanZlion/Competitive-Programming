class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        valid = False

        while stack:
            currNode, ptr = stack.pop()
            if ptr == len(word):
                valid = valid or currNode.isEndOfWord
                continue

            target = word[ptr]

            if target == ".":
                for childNode in currNode.children.values():
                    stack.append((childNode, ptr+1))

            elif target in currNode.children:
                stack.append((currNode.children[target], ptr+1))

        return valid