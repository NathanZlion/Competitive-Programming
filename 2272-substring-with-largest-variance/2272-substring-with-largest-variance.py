from collections import Counter
import string

class Solution:
    def largestVariance(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        
        # Try to maximize the occurrence of char1 and minimize char2
        for char1 in string.ascii_lowercase:
            for char2 in string.ascii_lowercase:
                if char1 == char2:
                    continue
                
                original_char1_freq = freq[char1]
                original_char2_freq = freq[char2]
                
                diff = 0
                seen_char1 = seen_char2 = False
                for char in s:
                    if char == char1 or char == char2:
                        if diff < 0:
                            # No more char1 left
                            if freq[char1] == 0:
                                break
                            
                            # No more char2 left
                            if freq[char2] == 0:
                                res = max(res, diff + freq[char1])
                                break

                            # We have both left, leave tha past aside :) and start over
                            diff = 0
                            seen_char1 = seen_char2 = False
                            
                        if char == char1:
                            seen_char1 = True
                            freq[char1] -= 1
                            diff += 1

                        if char == char2:
                            seen_char2 = True
                            freq[char2] -= 1
                            diff -= 1
                        
                        if seen_char1 and seen_char2:
                            res = max(res, diff)

                freq[char1] = original_char1_freq
                freq[char2] = original_char2_freq

        return res