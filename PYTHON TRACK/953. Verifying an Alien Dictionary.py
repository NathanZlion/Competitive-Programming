class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if (len(words) < 2):
            return True
        
        def greater(charA, charB):
            return order.index(charA) > order.index(charB)

        for ptr in range(len(words) - 1):
            word1 = words[ptr]
            word2 = words[ptr + 1]
            charPtr = 0

            if word1 == word2:
                continue
            while True:
                if (charPtr > len(word2) - 1):
                    return False

                elif (charPtr > len(word1) - 1):
                    return True

                elif (greater(word2[charPtr], word1[charPtr])):
                    break

                elif (word1[charPtr] == word2[charPtr]):
                    charPtr +=1

                else:
                    return False
        return True
