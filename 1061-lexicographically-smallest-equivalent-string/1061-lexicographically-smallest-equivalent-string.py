class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {char: char for char in ascii_lowercase}

        def find(char):
            """ Find with path compression """
            if rep[char] == char:
                return char

            root_rep = find(rep[char])
            rep[char] = root_rep

            return root_rep


        def union(char1, char2):
            """ Union to the smallest parent """
            rep1 = find(char1)
            rep2 = find(char2)
            min_parent = min(rep1, rep2)
            rep[rep1] = min_parent
            rep[rep2] = min_parent

        for index in range(len(s1)):
            union(s1[index], s2[index])

        return "".join([find(char) for char in baseStr])