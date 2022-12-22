class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        def similar(word1, word2):
            set1 = set(word1)
            set2 = set(word2)

            return set1 == set2

        ctr = 0
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                if (similar(words[i], words[j])):
                    ctr += 1

        return ctr
        
