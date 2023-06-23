class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # greed = minimum size cookie that the child will be content with
        
        """
        My thought process:
        - sort both arrays
        - move the pointer on the g when he's satisfied
        - move the pointer on the s when a child gets it or when it's not big enough to content a child
        """

        g.sort()
        s.sort()

        ptr2 = 0
        
        for ptr1 in range(len(g)):
            while ptr2 < len(s) and s[ptr2] < g[ptr1]:
                ptr2 += 1
            
            if ptr2 == len(s):
                break
            
            ptr1 += 1
            ptr2 += 1
        
        return ptr1
