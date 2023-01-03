class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """

        spaces = [0] + spaces + [len(s)]
        spaceLen = len(spaces) -1
        res = []
        ptr = 0
        while ptr < spaceLen:
            res.append(s[spaces[ptr]:spaces[ptr +1]])
            ptr += 1
        
        return " ".join(res)
