class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)

        @cache
        def subsequentTeams(reqTeamSize: int, maxRating: int, start: int, increasing: bool) -> int:
            if reqTeamSize == 0:
                return 1
            
            res = 0
            for index in range(start, n):
                if rating[index] > maxRating and increasing:
                    res += subsequentTeams(reqTeamSize - 1, rating[index], index+1, increasing)
                
                elif rating[index] < maxRating and not increasing:
                    res += subsequentTeams(reqTeamSize - 1, rating[index], index+1, increasing)
            
            return res

        res = 0
        for index in range(n-1, -1, -1):
            res += subsequentTeams(2, rating[index], index + 1, True)
            res += subsequentTeams(2, rating[index], index + 1, False)

        return res