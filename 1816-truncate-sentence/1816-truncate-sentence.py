class Solution(object):
    def truncateSentence(self, s, k):
        s.strip()
        s = s.split()
        return " ".join(s[:k])
        