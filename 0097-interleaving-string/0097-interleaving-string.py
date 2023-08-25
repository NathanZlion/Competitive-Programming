class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def canInterleave(ptr1: int, ptr2: int) -> bool:
            if ptr1 + ptr2 == len(s3):
                return True

            target = s3[ptr1+ptr2]
            if ptr1 == len(s1) and ptr2 != len(s2):
                return target == s2[ptr2] and canInterleave(ptr1, ptr2+1)

            if ptr2 == len(s2) and ptr1 != len(s1):
                return target == s1[ptr1] and canInterleave(ptr1+1, ptr2)

            if target == s1[ptr1] and target == s2[ptr2]:
                return canInterleave(ptr1+1, ptr2) or canInterleave(ptr1, ptr2+1)

            if target == s1[ptr1] and target != s2[ptr2]:
                return canInterleave(ptr1+1, ptr2)

            if target == s2[ptr2] and target != s1[ptr1]:
                return canInterleave(ptr1, ptr2+1)

            return False

        return canInterleave(0, 0)
