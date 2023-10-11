class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        n = len(ratings)
        upper_dps = [0] * n
        lower_dps = [0] * n

        count = 0
        for i in range(len(ratings)):
            for j in range(i):
                if ratings[j] < ratings[i]:
                    count += upper_dps[j]
                    upper_dps[i] += 1
                else:
                    count += lower_dps[j]
                    lower_dps[i] += 1

        return count