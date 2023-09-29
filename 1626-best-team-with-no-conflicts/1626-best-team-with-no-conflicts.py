class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = list(zip(ages, scores))
        players.sort()

        def dontConflict( youngerAge: int, youngerScore: int, olderAge: int, olderScore: int ) -> bool:
            return youngerAge == olderAge or youngerScore <= olderScore

        @cache
        def dp(i: int) -> int:
            currAge, currScore = players[i]
            maxScore = currScore
            for j in range(i-1, -1, -1):
                prevAge, prevScore = players[j]
                if dontConflict(prevAge, prevScore, currAge, currScore):
                    maxScore = max(maxScore, dp(j) + currScore)
            
            return maxScore

        max_score = 0
        for i in range(len(players)):
            max_score = max(max_score, dp(i))

        return max_score
