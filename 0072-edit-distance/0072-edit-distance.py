class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def dp(ptr1, ptr2) -> int:
            if ptr1 >= len(word1) or ptr2 >= len(word2):
                return len(word1) + len(word2) - ptr1 - ptr2
            
            if word1[ptr1] == word2[ptr2]:
                return dp(ptr1 + 1, ptr2 + 1)

            return 1 + min (
                dp(ptr1 + 1, ptr2 + 1),
                dp(ptr1, ptr2 + 1),
                dp(ptr1 + 1, ptr2),
            )

        return dp(0,0)