class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {
            len(s) : True
        }

        def can_segment(index: int) -> bool:
            if index in memo:
                return memo[index]

            for word in wordDict:
                # avoids out of bounds error
                if index + len(word) > len(s):
                    continue
                
                if s[index : index + len(word)] == word:
                    if can_segment(index + len(word)):
                        memo[index] = True
                        return True

            memo[index] = False
            return False
        
        return can_segment(0)
