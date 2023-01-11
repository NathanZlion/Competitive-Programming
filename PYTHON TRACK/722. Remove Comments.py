class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]

        use # to represent a new line
        
        things to check
        /* for a block comment
        // for a line comment
        """
        source_str = "#".join(source)
        comment_removed = []
        i = 0

        while i < len(source_str):
            symbol = source_str[i:i+2]
            if symbol == "//":
                # single line comment opened
                i += 2
                while i < len(source_str) and source_str[i] != "#":
                    i += 1
            elif symbol == "/*":
                i += 2
                while source_str[i:i+2] != "*/":
                    i += 1
                i += 2
            else:
                comment_removed.append(source_str[i])
                i += 1

        comment_removed = "".join(comment_removed).split("#")
        res = []

        for line in comment_removed:
            if line != "":
                res.append(str(line))

        return res
