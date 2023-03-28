class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0
        n, m = len(word1), len(word2)
        merged = []
        while ptr1 < n and ptr2 < m:
            if word1[ptr1] > word2[ptr2]:
                merged.append(word1[ptr1])
                ptr1 += 1
            
            elif word1[ptr1] < word2[ptr2]:
                merged.append(word2[ptr2])
                ptr2 += 1
            
            else:
                if word1[ptr1:] > word2[ptr2:]:
                    merged.append(word1[ptr1])
                    ptr1 += 1
                else:
                    merged.append(word2[ptr2])
                    ptr2 += 1
        
        merged.extend(word1[ptr1:])
        merged.extend(word2[ptr2:])
        
        return "".join(merged)
        

