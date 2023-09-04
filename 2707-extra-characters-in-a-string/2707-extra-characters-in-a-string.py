class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dict_set = set(dictionary)
        
        @cache
        def dp(start: int) -> int:
            if start == n:
                return 0
            
            # count this as a leftover character
            ans = dp(start+1) + 1
            for end in range(start, n):
                if s[start:end+1] in dict_set:
                    ans = min(ans, dp(end+1))

            return ans

        return dp(0)