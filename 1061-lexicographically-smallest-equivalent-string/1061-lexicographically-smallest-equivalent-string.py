class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # union every char by index of s1 and s2 and rep should be the minimum ord one
        # then find the minimum for all chars in baseStr
        parent = {}
        
        # for each character make it parent of it's own
        for charOrd in range(ord('a'), ord('z')+1):
            char = chr(charOrd)
            parent[char] = char

        def union(char1, char2):
            # to the minimum ordinance String
            par1 = representative(char1)
            par2 = representative(char2)
            
            if par1 > par2:
                parent[par1] = par2

            else:
                parent[par2] = par1

        def representative(char):
            # basecase
            if parent[char] == char:
                return char
            
            theParent = representative(parent[char])
            parent[char] = theParent
            return theParent
        
        for index in range(len(s1)):
            union(s1[index], s2[index])

        res = [representative(char) for char in baseStr]

        return "".join(res)
        