class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:        
        ptr1 = 0
        ptr2 = 0
        word1_len = len(word1)
        word2_len = len(word2)
        word1_turn = True
        ptr = 0
        res = [None for _ in range(word1_len + word2_len)]
        
        while ptr1 < word1_len and ptr2 < word2_len:
            if word1_turn:
                res[ptr] = word1[ptr1]
                ptr1 += 1
            else:
                res[ptr] = word2[ptr2]
                ptr2 += 1
                
            ptr += 1
            word1_turn = not word1_turn

        while ptr1 < word1_len:
            res[ptr] = word1[ptr1]
            ptr1 += 1
            ptr += 1

        while ptr2 < word2_len:
            res[ptr] = word2[ptr2]
            ptr2 += 1
            ptr += 1

        return "".join(res)