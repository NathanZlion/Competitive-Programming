class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)

        @cache
        def numOfTeamsForIncreasing(reqTeamSize: int, maxRating: int, start: int) -> int:
            if reqTeamSize == 0:
                return 1
            
            res = 0
            for index in range(start, n):
                if rating[index] > maxRating:
                    res += numOfTeamsForIncreasing(reqTeamSize - 1, rating[index], index+1)
            
            return res

        @cache
        def numOfTeamsForDecreasing(reqTeamSize: int, minRating: int, start: int) -> int:
            if reqTeamSize == 0:
                return 1
            
            res = 0
            for index in range(start, n):
                if rating[index] < minRating:
                    res += numOfTeamsForDecreasing(reqTeamSize - 1, rating[index], index+1)

            return res

        res = 0
        for index in range(n-1, -1, -1):
            res += numOfTeamsForIncreasing(2, rating[index], index + 1)
            res += numOfTeamsForDecreasing(2, rating[index], index + 1)

        return res