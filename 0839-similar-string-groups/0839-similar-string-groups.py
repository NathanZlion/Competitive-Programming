class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rep = {word: word for word in strs}

        def union(rep, word1, word2):
            word1_parent = find(rep, word1)
            rep[word1_parent] = find(rep, word2)

        def are_similar(word1, word2):
            diff_count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_count += 1
            
            return diff_count == 2
        
        def find(rep, word):

            while rep[word] != word:
                word = rep[word]

            return word

        n = len(strs)
        for i in range(n):
            word1 = strs[i]
            for j in range(i + 1, n):
                word2 = strs[j]
                if are_similar(word1, word2):
                    union(rep, word1, word2)
                    

        return len(set([find(rep, word) for word in strs]))