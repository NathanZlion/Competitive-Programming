class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ptr = 0
        res = ""

        while (ptr < len(word1) and ptr < len(word2)):
            res += word1[ptr]
            res += word2[ptr]
            ptr +=1
        
        if (ptr < len(word1)):
            res += word1[ptr:]

        if (ptr < len(word2)):
            res += word2[ptr:]
        
        return res
