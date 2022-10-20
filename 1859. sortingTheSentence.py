class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = s.split(" ")
        output = [""] * len(s)
        for word in s:
            output[int(word[-1]) -1] = word[:-1]

        sentence =""
        for words in output:
            sentence += (words + " ")

        return sentence.strip()     
