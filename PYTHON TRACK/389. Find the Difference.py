class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        freq = {}
        for letter in s:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        
        for letter in t:
            if (letter in freq):
                if (freq[letter] > 1):
                    freq[letter] -= 1
                else:
                    del freq[letter]
            else:
                return letter
