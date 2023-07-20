class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        
        def is_contained(word, start_index):
            for index in range(len(word)):
                if word[index] != s[start_index + index]:
                    return False

            return True

        def can_segment(index: int) -> bool:
            if index in memo:
                return memo[index]

            for word in wordDict:
                # avoids out of bounds error
                if index + len(word) > len(s):
                    continue
                
                if is_contained(word, index):
                    if can_segment(index + len(word)):
                        memo[index] = True
                        return True

            memo[index] = False
            return False
        
        return can_segment(0)
